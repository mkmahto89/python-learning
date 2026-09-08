from fastapi import FastAPI,HTTPException

app=FastAPI()

items=[]
@app.get("/")
def root():
    return "hello FAST API"

@app.post("/items")
def create_item(item:str):
    items.append(item)
    return items

@app.get("/items")
def get_list_item(limit:int):
    return items[:limit]

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id>len(items):
        raise HTTPException(status_code=404,detail="item not found")
    item=items[item_id]
    return item  


 




#uvicorn Main_FAST_API:app --reload   
#curl http://127.0.0.1:8000/ 
#curl -X POST http://127.0.0.1:8000/items?item=abc
#curl -X GET http://127.0.0.1:8000/items/0
#curl -X GET http://127.0.0.1:8000/items?limit=2

my=[1,2,3]

for m in my:
    print(m)