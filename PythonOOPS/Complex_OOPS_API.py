
"""
Extremely complex production-style Python backend (FastAPI + Async Stack)
Demonstrates: async everything, sagas, distributed locks, CQRS-ish commands,
background jobs, caching, auth, resilience patterns, concurrent fan-out.
"""

from __future__ import annotations

import asyncio
import hashlib
import logging
import time
import uuid
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Annotated, Any, AsyncGenerator, Optional

import redis.asyncio as aioredis
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Request,
    status,
)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    select,
    update,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from jose import JWTError, jwt
from passlib.context import CryptContext

# ---------------------------------------------------------------------------
# Settings & Logging
# ---------------------------------------------------------------------------

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:pass@localhost/complex_db"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "super-secret-key-change-me-in-prod"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    max_concurrent_external_calls: int = 20
    rate_limit_per_minute: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
logger = logging.getLogger("complex_backend")
logging.basicConfig(level=logging.INFO)

# ---------------------------------------------------------------------------
# Database Models
# ---------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role: Mapped[str] = mapped_column(String(50), default="user")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(String(50), default="pending")
    total_amount: Mapped[int] = mapped_column(Integer)  # cents
    inventory_reserved: Mapped[bool] = mapped_column(Boolean, default=False)
    payment_processed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=lambda: datetime.now(timezone.utc))


class InventoryItem(Base):
    __tablename__ = "inventory"
    sku: Mapped[str] = mapped_column(String(100), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, default=0)
    reserved: Mapped[int] = mapped_column(Integer, default=0)


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------

class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class OrderCreate(BaseModel):
    items: list[dict[str, Any]]  # [{"sku": "...", "qty": 2}, ...]
    total_amount: int = Field(..., gt=0)

    @field_validator("items")
    @classmethod
    def validate_items(cls, v: list) -> list:
        if not v:
            raise ValueError("Order must contain at least one item")
        return v


class OrderResponse(BaseModel):
    id: str
    status: str
    total_amount: int
    created_at: datetime


# ---------------------------------------------------------------------------
# Core Infrastructure
# ---------------------------------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

engine = create_async_engine(settings.database_url, echo=False, pool_size=20, max_overflow=10)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

redis_client: Optional[aioredis.Redis] = None
semaphore = asyncio.Semaphore(settings.max_concurrent_external_calls)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global redis_client
    redis_client = aioredis.from_url(settings.redis_url, decode_responses=True)
    # In real life: run migrations, warm caches, start background workers
    logger.info("Complex backend starting up...")
    yield
    await redis_client.close()
    await engine.dispose()
    logger.info("Complex backend shut down.")


app = FastAPI(title="Most Complex Python Backend Demo", lifespan=lifespan)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


# ---------------------------------------------------------------------------
# Auth Utilities
# ---------------------------------------------------------------------------

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.secret_key, algorithm="HS256")


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.secret_key, algorithm="HS256")


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:
    try:
        payload = jwt.decode(credentials.credentials, settings.secret_key, algorithms=["HS256"])
        if payload.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token type")
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="User inactive or not found")
    return user


# ---------------------------------------------------------------------------
# Distributed Lock (Redis)
# ---------------------------------------------------------------------------

class DistributedLock:
    def __init__(self, key: str, timeout: int = 10):
        self.key = f"lock:{key}"
        self.timeout = timeout
        self.token = str(uuid.uuid4())

    async def __aenter__(self):
        end = time.time() + self.timeout
        while time.time() < end:
            if await redis_client.set(self.key, self.token, nx=True, ex=self.timeout):
                return self
            await asyncio.sleep(0.05)
        raise HTTPException(status_code=409, detail="Could not acquire lock")

    async def __aexit__(self, exc_type, exc, tb):
        # Safe release with Lua-style check
        current = await redis_client.get(self.key)
        if current == self.token:
            await redis_client.delete(self.key)


# ---------------------------------------------------------------------------
# Saga / Compensating Transaction Pattern (Order Placement)
# ---------------------------------------------------------------------------

class OrderSaga:
    """Classic distributed transaction saga with compensations."""

    def __init__(self, db: AsyncSession, user: User, order_data: OrderCreate):
        self.db = db
        self.user = user
        self.order_data = order_data
        self.order: Optional[Order] = None
        self.steps_completed: list[str] = []

    async def execute(self) -> Order:
        try:
            await self._create_order()
            await self._reserve_inventory()
            await self._process_payment()
            await self._finalize()
            return self.order
        except Exception as e:
            logger.exception("Saga failed, compensating...")
            await self._compensate()
            raise HTTPException(status_code=400, detail=f"Order failed: {str(e)}")

    async def _create_order(self):
        self.order = Order(
            user_id=self.user.id,
            total_amount=self.order_data.total_amount,
            status="pending",
        )
        self.db.add(self.order)
        await self.db.flush()
        self.steps_completed.append("order_created")

    async def _reserve_inventory(self):
        async with DistributedLock(f"inventory:{self.order.id}"):
            for item in self.order_data.items:
                result = await self.db.execute(
                    select(InventoryItem).where(InventoryItem.sku == item["sku"]).with_for_update()
                )
                inv = result.scalar_one_or_none()
                if not inv or inv.quantity - inv.reserved < item["qty"]:
                    raise ValueError(f"Insufficient stock for {item['sku']}")
                inv.reserved += item["qty"]
            self.order.inventory_reserved = True
            self.steps_completed.append("inventory_reserved")

    async def _process_payment(self):
        # Simulate external payment gateway with timeout + circuit style
        async with semaphore:
            await asyncio.sleep(0.3)  # pretend network call
            # In real life: call Stripe/PayPal with retries + circuit breaker
            if self.order.total_amount > 1_000_000:  # artificial failure
                raise ValueError("Payment declined")
            self.order.payment_processed = True
            self.steps_completed.append("payment_processed")

    async def _finalize(self):
        self.order.status = "confirmed"
        # Publish event (in real system → RabbitMQ/Kafka)
        await redis_client.publish("order.events", f"order.confirmed:{self.order.id}")
        self.steps_completed.append("finalized")

    async def _compensate(self):
        if "inventory_reserved" in self.steps_completed and self.order:
            for item in self.order_data.items:
                await self.db.execute(
                    update(InventoryItem)
                    .where(InventoryItem.sku == item["sku"])
                    .values(reserved=InventoryItem.reserved - item["qty"])
                )
        if self.order:
            self.order.status = "cancelled"
            self.order.inventory_reserved = False
            self.order.payment_processed = False


# ---------------------------------------------------------------------------
# Caching + Rate Limiting Helpers
# ---------------------------------------------------------------------------

async def rate_limit(user_id: int):
    key = f"rate:{user_id}:{int(time.time() // 60)}"
    count = await redis_client.incr(key)
    if count == 1:
        await redis_client.expire(key, 60)
    if count > settings.rate_limit_per_minute:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")


async def cache_get_or_set(key: str, ttl: int, factory):
    cached = await redis_client.get(key)
    if cached:
        return cached
    value = await factory()
    await redis_client.setex(key, ttl, value)
    return value


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.post("/auth/login", response_model=TokenPair)
async def login(email: str, password: str, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not pwd_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = create_access_token({"sub": user.id, "role": user.role})
    refresh = create_refresh_token({"sub": user.id})
    return TokenPair(access_token=access, refresh_token=refresh)


@app.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    order_in: OrderCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    await rate_limit(current_user.id)

    # Concurrent external enrichment example (fan-out)
    async def enrich(sku: str):
        async with semaphore:
            await asyncio.sleep(0.1)
            return {"sku": sku, "meta": f"enriched-{sku}"}

    enriched = await asyncio.gather(*[enrich(i["sku"]) for i in order_in.items])

    saga = OrderSaga(db, current_user, order_in)
    order = await saga.execute()

    # Invalidate related caches
    await redis_client.delete(f"user_orders:{current_user.id}")

    return OrderResponse(
        id=order.id,
        status=order.status,
        total_amount=order.total_amount,
        created_at=order.created_at,
    )


@app.get("/orders/me")
async def my_orders(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    cache_key = f"user_orders:{current_user.id}"

    async def fetch():
        result = await db.execute(
            select(Order).where(Order.user_id == current_user.id).order_by(Order.created_at.desc())
        )
        orders = result.scalars().all()
        return str([{"id": o.id, "status": o.status} for o in orders])

    return await cache_get_or_set(cache_key, 30, fetch)


# ---------------------------------------------------------------------------
# Background Job Simulation (would be ARQ / Celery / Dramatiq in real life)
# ---------------------------------------------------------------------------

async def process_heavy_analytics(order_id: str):
    """Example of a long-running background job."""
    await asyncio.sleep(5)
    logger.info(f"Analytics completed for order {order_id}")


@app.post("/orders/{order_id}/analyze")
async def trigger_analytics(
    order_id: str,
    current_user: Annotated[User, Depends(get_current_user)],
):
    # In production: enqueue to Redis/ARQ/Celery
    asyncio.create_task(process_heavy_analytics(order_id))
    return {"status": "queued"}


# ---------------------------------------------------------------------------
# Health + Metrics
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    try:
        await redis_client.ping()
        async with engine.connect() as conn:
            await conn.execute(select(1))
        return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, workers=1)