""""
class emp:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property
    def getname1(self):
        return self.__name

    @property
    def getage1(self):
        return self.__age

    @getname1.setter
    def getname1(self,name):
        self.__name=name
        
    @getage1.setter
    def getage1(self,age):
        self.__age=age

e=emp('mohit',22)
print(e.getname1)
print(e.getage1)
e.name='ram'
e.age=22
print(e.getname1)
print(e.getage1)

class MyClass:
    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

obj = MyClass()

#composition means has a relationship

class CPU:
    def process(self):
        print('execute process')
class Monitor:
    def display(self):
        print('display picture')
class Computer:
    def __init__(self):
        self.c=CPU()
        self.m=Monitor()

    def StartComputer(self):
        self.c.process()
        self.m.display()

comp=Computer()
comp.StartComputer()

##operator over loading
class Pt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Pt(self.x+other.x,self.y+other.y)
    def dis(self):
        print(self.x,self.y)

p1=Pt(2,3)
p2=Pt(4,5)
p3=p1+p2
p3.dis()

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"{self.x},{self.y}"    

    def __repr__(self):
        return f"{self.x},{self.y}"        
        

V1=Vector(1,2)
V2=Vector(3,4)
V3=Vector(5,6)
V4=Vector(7,8)
VSum=V1+V2+V3+V4
print(VSum)


def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

def hello():
    print("Hello")

new_func = decorator(hello)

new_func()  

print('#######')

##
def deco(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@deco
def hello():
    print("Hello")


hello()

def argsfun(*mohit,**karthik):
    print(mohit[0])
    print(mohit[1])
    print(mohit[2])
    print(karthik['a1'])
    print(karthik['a2'])
    print(karthik['a3'])


argsfun(1,2,'three',a1='test1',a2='test2',a3='test3')   
 
import csv
data=[
["Name","Age","Salary"]
,["Mohit","21","1000"]
,["Raj","22","2000"]
,["Mohan","23","3000"]


]
def MyFileWrite():
    with open("PythonCSV.txt","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(data)

MyFileWrite()    

def MyFileRead():
    with open("PythonCSV.txt","r") as f:
        reader=csv.reader(f)
        for rw in reader:
            print(rw)

MyFileRead()   

import pandas as pd
def MyPanda():
    df=pd.read_csv("PythonCSV.txt")
    print(df)

MyPanda()  

import pandas as pd
def MyPandasLearn():
    df=pd.read_csv("PythonCSV.txt")
    #print(df.head())
    #rint(df.tail())
    #print(df[["Name","Age"]])
    #print(df[df["Age"]>21])
    #df["Age"]=pd.to_numeric(df["Age"], errors="coerce")
    #print(df["Age"].value_counts())
    #print(df.iloc[:, -1])
    #print(df.iloc[:, -2])
    #print(df.iloc[:, -3])
    #print(df.iloc[:,1])
    print(pd.crosstab(df["Name"], df["Age"]))
    print(df.describe())
    print(df.info())




MyPandasLearn()    

from abc import ABC,abstractmethod     

class BankAccount(ABC):
    def __init__(self,account_number,balance,owner)
        self.__account_number=account_number
        self.__balance=balance
        self.__owner=owner

    @abstractmethod
    def deposit(self)
        pass 
    @abstractmethod   
    def withdraw(self)
        pass
    @abstractmethod
    def calculate_interrest(self)
        pass

    def get_balance(self)
        return __balance

    def transfer(self)
        pass

class SavingsAccount(BankAccount):

class CurrentAccount(BankAccount):

class FixedDepositAccount(SavingsAccount):

class Employee:
    def __init__(self,name):
        self._name=name 

    @property
    def getsetname(self):
        return self._name

    @getsetname.setter
    def getsetname(self,name):
        self._name=name  

    @getsetname.deleter
    def getsetname(self):
        del self._name    




e=Employee('mohit')
print(e.getsetname)
e.getsetname='raj'

del e.getsetname
print(e.getsetname)

class Emp:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Emp(self.x+other.x,self.y+other.y)

e1=Emp(2,3)
e2=Emp(3,5)
e=e1+e2
print(e.x)
print(e.y)

class Company:
    def __init__(self,companyname):
        self._companyname=companyname

class Employee(Company):
    def __init__(self,name,age,companyname):
        super().__init__(companyname)
        self.__name=name
        self.__age=age


e=Employee('mohit',21,'abc')
print(e._companyname)

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def display(self,name):
        pass

class PF(Employee):
    def display(self,name):
        print(name)

E=PF()
E.display('mohit')  
 

class Emp(object):

    __slots__=["_name","age"]
    def __init__(self,name):
        self._name=name



E=Emp('mohit')
E.city='jbp'  
print(E.city)   

class Emp(object):
    pass

e=Emp()

print(type(e))
print(type(Emp))
print(type(type))

class Greeter:
    def hello(self):
        print("Hi")

#metaclass internal
Greeter = type(
    "Greeter",     # 1. class name (string)
    (),            # 2. base classes (tuple)
    {              # 3. class body (namespace dict)
        "hello": lambda self: print("Hi")
    }
)  

g=Greeter()
g.hello()

class Emp:
    def __init__(self,x):
        self._x=x

    def __call__(self):
        print(self._x)

e=Emp(5)
e()      

import yfinance as yf
import pandas as pd

data = yf.download("AAPL", start="2023-01-01")    
df=pd.DataFrame(data)
print(df.head())
print(df.iloc[0])

class Emp:
    CompanyName='xyz'

    def __init__(self,x,y):
        self.x=x
        self.y=y

    @classmethod
    def display(cls):
        print(cls.CompanyName)

E=Emp(2,3)
E.CompanyName='ABC'
print(E.CompanyName)
print(Emp.CompanyName)
Emp.CompanyName='PQR'
print(Emp.CompanyName)

class Emp:

    myvar=2

    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def mystatic(self,self2,a,b):
        return self.x+self.y+self2.myvar+a+b

E=Emp(2,3)

print(Emp.mystatic(E,Emp,2,3))

from abc import ABC,abstractmethod

class Bank(ABC):

    def __init__(self,balance):
        self.__balance=balance

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def checkbalance():
        pass

class Transaction(Bank):

    def deposit(self,amount):
        self._Bank__balance=amount+self._Bank__balance

    def checkbalance(self):
        return self._Bank__balance  

b=Bank(0)   

#private method
class Emp:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __MyMethod(self):
        print(self.x)

E=Emp(1,2)
E._Emp__MyMethod()
 
#duck typing ,if object is of type then it will behave like that type  
class CDPlayer:

    def playsound(self):
        print('playing sound in CD player')

class USBPlayer:

    def playsound(self):
        print('playing sound in USBplayer')


def testplay(sound):
        sound.playsound()

C=CDPlayer()
U=USBPlayer()

C.playsound()

import pandas as pd
def MyPandasLearn():

    try:    
        df=pd.read_csv("PythonCSV.txt")
        print(df.head())
        #rint(df.tail())
        #print(df[["Name","Age"]])
        #print(df[df["Age"]>21])
        #df["Age"]=pd.to_numeric(df["Age"], errors="coerce")
        #print(df["Age"].value_counts())
        #print(df.iloc[:, -1])
        #print(df.iloc[:, -2])
        #print(df.iloc[:, -3])
        #print(df.iloc[:,1])
        #print(pd.crosstab(df["Name"], df["Age"]))
        #print(df.describe())
        #print(df.info())
    except:
        print('error')    

class Office:
    def __init__(self,OfficeName,OfficeLocation):
        self.OfficeName=OfficeName
        self.OfficeLocation=OfficeLocation

class Employee:
    def __init__(self,EmployeeName,EmployeeAge):
        self.EmployeeName=EmployeeName
        self.EmployeeAge=EmployeeAge

class SiliconValley:
    def __init__(self,OfficeName,OfficeLocation,EmployeeName,EmployeeAge):
        A=Office(OfficeName,OfficeLocation)
        B=Employee(EmployeeName,EmployeeAge)
        print(A.OfficeName)
        print(A.OfficeLocation)
        print(B.EmployeeName)
        print(B.EmployeeAge)

S=SiliconValley('New Jersey','Google','Sundar Pichae',45)


#duck typing 
class VSCode:
    def execute(self):
        print('running into VS code')
class PyCharm:
    def execute(self):
        print('running into pycharm')
class Spyder:
    def execute(self):
        print('running into Spyder')
class ExecuteCode:
    def __init__(self,obj):
        obj.execute()

V=VSCode()
P=PyCharm()
S=Spyder()

E=ExecuteCode(V)
E=ExecuteCode(P)
E=ExecuteCode(S)

#inheritance

class GrandFather:
    def Name(self):
        print('i am grandfather')
class Father(GrandFather):
    def Name(self):
        print('i am father')  
class Child(Father):
    def Name(self):
        print('i am child')

ty=[Child(),Father(),GrandFather()]

for ob in ty:
    ob.Name()

class Office:
    def __init__(self,OfficeName,OfficeLocation):
        self.OfficeName=OfficeName
        self.OfficeLocation=OfficeLocation

class Employee:
    def __init__(self,EmployeeName,EmployeeAge):
        self.EmployeeName=EmployeeName
        self.EmployeeAge=EmployeeAge

class SiliconValley:
    def __init__(self,OfficeName,OfficeLocation,EmployeeName,EmployeeAge):
        self.A=Office(OfficeName,OfficeLocation)
        self.B=Employee(EmployeeName,EmployeeAge)

    def display(self):    
        print(self.A.OfficeName)
        print(self.A.OfficeLocation)
        print(self.B.EmployeeName)
        print(self.B.EmployeeAge)

S=SiliconValley('New Jersey','Google','Sundar Pichae',45)
S.display()


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

import psutil as pt

print(pt.virtual_memory())
print(10%7)  # give the remainder
print(10/7)  # give the quotient means 1.4625632 but in decimal
print(10//7) # give the quotient but in whole no 

class Employee:
    def myprint(self):
        print('mohit')

    def __call__(self):
        print('rohit')

E=Employee()
E()
 
class Singleton:
    instance=None

    def __new__(cls):
        if cls.instance==None:
            cls.instance=super().__new__(cls)

        return cls.instance

E=Singleton()
E2=Singleton()

if(E==E2):
    print('same object instance')
else:
    print('different object instance')    


class Singleton_1:
    pass

E=Singleton_1()
E2=Singleton_1()

if(E==E2):
    print('same object instance')
else:
    print('different object instance')   


#concept: if no method is overriden  in child class and object of child class is
# created  and method and called then it will first go to child class to find that method
# and if that method is not exists then it will go to parent class 
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 120)
bus1.display()

#decorator: its used to modfied the existing function by wrapping changes around that 

def MyMethodModified(func):
    def wrapper():
        print('before modification call')
        func()
        print('after modification')
    return wrapper    



@MyMethodModified
def Greet():
    print('welcome')

Greet()    

# slots are used to pre declare attribute in class to save memory
# and restrict more declaration  and improve performance 
print(f'') # will treated as formatted string and dynamic variable will be replaced
class Employee:
    __slots__=["name","age"]
    def __init__(self,name,age):
        self.name=name
        self.age=age

E=Employee('mohit',21)  
print(f"name is {E.name} age is {E.age}")      

class CPU:
    def Process(self):
        print("execute process")
class Driver:
    def Drivers(self):
        print("managing hardware")

class Computer:
    def start(self):
        self.P=CPU()
        self.D=Driver()

C=Computer()
print(C.start())
print(C.P.Process()) 

class Employee:
    def __init__(self,x):
        self.x=x  

    def __len__(self):
        return int((len(self.x)))

E=Employee('12345')
print(len(E))

class MyMeta(type):

    instance=None
    def method_1(cls):
        print("method 1")
    def method_2(cls):
        print("method 2")  
    def __new__(msc,name,bases,namespace):
        namespace["x"]=10
        namespace["y"]=20
        namespace["method_1"]=msc.method_1   
        namespace["method_2"]=msc.method_2
        return super().__new__(msc,name,bases,namespace)    

class Employee(metaclass=MyMeta):
    pass

E=Employee()
print(E.x)
E.method_1()
E2=Employee()
print(E)
print(E2)

class Singleton:

    _instance=None
    def __new__(cls):
        if cls._instance==None:
            print('new instance going to create')
            cls._instance=super().__new__(cls)
        else:
            print('same instance used')
        return cls._instance        


    def __init__(self):
        print('init called')

S=Singleton()
S2=Singleton()

A = type.__new__(type, "A", bases, namespace)
type.__init__(A, "A", bases, namespace)

here type is default meteclass  that control 


--------------------------------IMP-----------------------
type is directly responsible for creating classes
When Python executes:
class Employee:
    pass
it effectively does:
Employee = type("Employee", (), {})

()->tuple contains base classes
{}->set that contains attribute  and methods

So type creates the class object.
For creating objects (instances)

When you do:
e = Employee()
Python calls the metaclass's __call__ method.
Since Employee was created by type, its metaclass is type:
type.__call__(Employee)

Then type.__call__ internally does:
obj = Employee.__new__(Employee)
Employee.__init__(obj)

So:
type does not directly create the instance
type.__call__ orchestrates the process
Employee.__new__ actually creates the instance
Employee.__init__ initializes it
------------------------------------------------------------

class A:
    def __new__(cls):
        print("__new__")
        return super().__new__(cls)

    def __init__(self):
        print("__init__")

A()
so below happen internally 

obj = A.__new__(A)

if isinstance(obj, A):
    A.__init__(obj)

return obj

type.__call__()
    ├── calls Class.__new__()
    ├── if returned object is instance of Class
    │       └── calls Class.__init__()
    └── returns object


#Problem Statement: Write a Python program to create a Notebook class that 
#maintains an internal list of notes. Add an add_note(note) method that appends a new note to the list
#, and a show_notes() method that prints all stored notes.
# enumerate give index also while position the number 

class Notebook:

    def __init__(self):
        self.nt=[]

    def add_notes(self,nots):
        self.nt.append(nots)

    def show_notes(self):
        for notes in self.nt:
            print(notes)

        for idx,notes in enumerate(self.nt,start=1):   
            print(f"{idx} . {notes}")

N=Notebook()
N.add_notes("this is my notes")
N.show_notes()
N.add_notes(input("enter your note"))
N.show_notes()


Problem Statement: Write a Python program to create a CoffeeMachine class 
that tracks three resource attributes: water, coffee, and milk (in ml/g). 
Add a make_latte() method that checks whether sufficient resources are available, 
deducts them if so, and prints an appropriate message in either case.

class CoffeeMachine:
        def __init__(self,water,milk,coffee):
            self.water=water
            self.coffee=coffee
            self.milk=milk

        def make_latte(self):
            WaterNeeded=200
            CoffeeNeeded=50
            MilkNeeded=100

            if self.water>WaterNeeded and self.coffee>CoffeeNeeded and self.milk>MilkNeeded:
                self.water=self.water-WaterNeeded
                self.coffee=self.coffee-CoffeeNeeded
                self.milk=self.milk-MilkNeeded
                print('coffee created') 
                print(f"Remaining Water:{self.water}, Coffee:{self.coffee}, Milk:{self.milk}")  
            else:
                print('not sufficient resources')   
                print(f"Remaining Water:{self.water}, Coffee:{self.coffee}, Milk:{self.milk}")   

C=CoffeeMachine(1000,500,250)
C.make_latte()
C.make_latte()
C.make_latte()
C.make_latte()
C.make_latte()
C.make_latte()
C.make_latte()
"""
"""
write a Python program to create a Vehicle class with a class attribute color = "White" 
that is shared by all instances. Create two vehicle objects and demonstrate that both 
share the same default color, then show that changing the class attribute updates all instances that have not overridden it.

class Vechile:
    DefualtColor="White"

    def __init__(self,color):
        self.color=color

V1=Vechile("Black")
V2=Vechile("Blue")
print(f" instance color for v1 {V1.color}")  
print(f" instance color for v2 {V2.color} ")
print(f"object instance with class attribute v1 {V1.DefualtColor}")
print(f"object instance with class attribute v2 {V2.DefualtColor}")
Vechile.DefualtColor="Green"
print(f"object instance with class attribute v1 {V1.DefualtColor}")
print(f"object instance with class attribute v2 {V2.DefualtColor}")


Problem Statement: Write a Python program to create a Vehicle parent 
class with name and max_speed attributes and a display() method. 
Then create a Bus child class that inherits everything from Vehicle without adding anything new, 
and confirm that an instance of Bus can access the parents method.

class Vechile:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed=max_speed

    def display(self):
        print(f"vechile name is:{self.name} , max speed is {self.max_speed}")  

class Bus(Vechile):
    pass

B=Bus("tata harrier",150)
B.display()

Problem Statement: Write a Python program where a Vehicle parent 
class has a seating_capacity() method that accepts a capacity argument.
 Create a Bus child class that overrides this method to provide a default 
 seating capacity of 50, using super() to call the parents version internally.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)

bus = Bus("School Bus", 120)
bus.seating_capacity()

Problem Statement: Write a Python program that creates a Vehicle parent 
class with a base fare, then extends a Taxi child class that adds a 10%
 maintenance fee on top of the base fare using super().

class Vechile:
    def __init__(self,base_fare):
        self.base_fare=base_fare

class Taxi(Vechile):
    def __init__(self,base_fare):
        super().__init__(base_fare+(.10*base_fare))

T=Taxi(100)
print(T.base_fare)

#DIP
class Database:
    def connect(self):
        pass        

class MySQL(Database):
    def connect(self):
        print ("connecting to MySQL")

class SQL(Database):
    def connect(self):
        print("connecting to SQL")

class Oracle(Database):
    def connect(self):
        print("connecting to Orocle")

class MongoDB(Database):
    def connect(self):
        print("connect to MongoDB")

class Application:
    def __init__(self,db:Database):
        self.db=db

    def start(self):
        self.db.connect()
    

S=SQL()
A=Application(a1)
A.start()


#####

Why this design is good
✔ 1. Encapsulation
Coordinates are stored inside the object.
✔ 2. Open/Closed Principle (SOLID)
You can add new shapes without modifying Shape.
✔ 3. Validation per shape
Each shape enforces its own rules.
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self._validate()

    @abstractmethod
    def _validate(self):
        pass


class Circle(Shape):
    def _validate(self):
        if len(self.coordinates) != 1:
            raise ValueError("Circle needs center point only")


#factory pattern
from abc import ABC,abstractmethod

class vechile(ABC):
    @abstractmethod
    def driving(self):
        pass

class car(vechile):
    def driving(self):
        print("driving a car..")

class bike(vechile):
    def driving(self):
        print("driving a bike..")

class truck(vechile):
    def driving(self):
        print("driving a truck..")

class ClassFactory:

    @staticmethod
    def GetFactoryBasedObj(vechiletype:str)->vechile:
        if vechiletype=="car":
            return car()
        elif vechiletype=="bike":
            return bike()
        elif vechiletype=="truck":
            return truck()
        else:    
            raise print("no valid choice")

ob=ClassFactory.GetFactoryBasedObj("car")
ob.driving()

from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(PaymentProcessor):
    def pay(self,msg):
        print(f"payment is process via: {msg} method")

class BankNEFT(PaymentProcessor):
    def pay(self,msg):
        print(f"payment is process via: {msg} method")

class BankRTGS(PaymentProcessor):
    def pay(self,msg):
        print(f"payment is process via: {msg} method")


class SelectPaymentMethod:
    @staticmethod
    def MethodOfPayment(str):
        if str=="UPI":
            return UPI()
        elif str=="BankNEFT":
            return BankNEFT()
        elif str=="BankRTGS":
            return BankRTGS()
        else:
            return ValueError("class not found")

class ApplicationPaymentInterface:
    #injection
    def __init__(self,PaymentTypeObj):
        self.PaymentTypeObj=PaymentTypeObj

    def PaymentExecution(self,msg):
        self.PaymentTypeObj.pay(msg)

RTGS=SelectPaymentMethod.MethodOfPayment("BankRTGS")
App=ApplicationPaymentInterface(RTGS)
App.PaymentExecution("RGTS")

class MyMeta(type):
    def __new__(cls,self,bases,namespace):
        namespace["var"]="mohit"
        return super().__new__(cls,self,bases,namespace)

class MyClass(metaclass=MyMeta):
    def MyPrint(self):
        print(f"value passed from metaclass: {self.var}")

M=MyClass()
M.MyPrint()

from MyEmployee import Employee
class Company:

     
    def __init__(self):
        self.Emplst=[]

    def AddEmp(self,new_employee):
        self.Emplst.append(new_employee) 

    def DisplayEmp(self):
        for i in self.Emplst:
            print(f"EmpName is:{i.name} and Age:{i.age}")
        print('------------')    

def main():
    C=Company()
    E=Employee("mohit",23,50000)
    C.AddEmp(E)
    E=Employee("Raj",23,40000)
    C.AddEmp(E)
    C.DisplayEmp()

main()


Library Management System
    Design classes for:
Book
Member
Librarian
Library
    Requirements:
Issue book
Return book
Track availability
    Concepts:
Encapsulation
Composition
Inheritance

class Library:
        def __init__(self):
            l=librarian()
            bk=Book()
            m=Member()



class Book(Library):
    def __init__(self,bookname_val,author_val)
        self.bookname=bookname_val
        self.author=author_val
        

class Librarian:
    def issuebook(self)
        pass

    def returnbook(self)
        pass

    def trackavailability(self)
        pass


class Member:
    pass


from dataclasses import dataclass

@dataclass
class Employee:
        name:str
        age:int

E=Employee("mohit",23)
print(E)
print(E.name)
 
import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for i in range(n):
        matrix.append(input())

        

#print(len(matrix))    

 
for i in range(len(matrix)):
    print(matrix[i])
    for j in range(len(matrix[i])):
        #print(matrix[i][j])
        continue
 
str=''
for i in range(0,m):
        for j in range(0,n):
            str=str+matrix[j][i]


print(str)

class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        self.avg=0

    def add_marks(marks):
        self.marks.append(marks)

    def average(self):
        for i in self.marks:
            self.avg+=i

        self.avg=self.avg//len(self.marks)    

        return self.avg

    def result(self):
        avg=self.average()
        if self.avg>=40:
            print("Pass")
        else:
            print("Fail")     
  
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        if book!='' and book not in self.books:
            self.books.append(book)

    def remove_book(self,book):
        if book!='' and book in self.books:
            self.books.remove(book)   

    def show_books(self):
        for b in self.books:
            print(b)  


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def give_raise(self,percent):
        if percent>0:
            self.salary=self.salary+((percent/100)*self.salary)


    def annual_salary(self):
        return self.salary*12   

    def display(self):
        print(f"Name of the Employee is:{self.name} and Annual salary is:{self.annual_salary()}")      


class MyCart:
    def __init__(self,item,quantity,price):
        self.item=item
        self.quanity=quantity
        self.price=price

class Cart:
    def __init__(self,obj:MyCart):
        self.MyCartObj=obj()
        self.items={}]

    def add_items(self):
        self.items.add(MyCart)    

    def remove_items(self,item)
        if len(self.items)>0:
            self.items.remove[item]

    def calculate_total_bill(self):
        total=0
        for i , j, k in self.items
            total=total+(j*k)

        return total

    def show_items(self):
        for i , j , k in self.items
            print(i)                      


class MyCart:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, cart_item):
        if cart_item.price >= 0:
            self.items[cart_item.item] = cart_item

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def calculate_total_bill(self):
        total = 0

        for item in self.items.values():
            total += item.quantity * item.price

        return total

    def show_items(self):
        for item in self.items.values():
            print(item.item, item.quantity, item.price)


class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock

    def update_price(self,price):
        self.price=price

    def add_stock(self,quantity):
        self.stock+=quantity

    def remove_stock(self,quantity):
        if quantity>self.stock:
            print("insufficient stock")
        else:    
            self.stock-=quantity    

    def display(self):
        return f"ProductID: {self.product_id} Name:{self.name} Price:{self.price} Stock:{self.stock}"

class Inventory:
    def __init__(self):
        self.Products={}

    def add_product(self,pd):
        if pd.product_id not in self.Products:
            self.Products[pd.product_id]=pd

    def remove_product(self,product_id):
        if product_id  in self.Products:
            del self.Products[product_id]

    def search(self,product_id):
        Prod=None
        for i in self.Products.values():
            if i.product_id==product_id:
                    Prod=i
            break
        return Prod    

    def total_inventory_value(self):
        for i in self.Products:
            print ("ProductID:"+str(self.Products[i].product_id)+" : "+ str(self.Products[i].price*self.Products[i].stock))   

    def display_product_name(self):
        for i in self.Products.values():
            print(i.name)          

    def display_all(self):
        for i in self.Products.values():
            #print ("ProductID:"+str(self.Products[i].product_id)+ " Name:"+self.Products[i].name+" Price:"+str(self.Products[i].price)+" Stock:"+str(self.Products[i].stock) )
            print(i.display())

p1 = Product(101, "Laptop", 50000, 5)
p2 = Product(102, "Mouse", 500, 20)



inv = Inventory()

inv.add_product(p1)
inv.add_product(p2)

#inv.remove_product(101)
#print(inv.search(101))
#print(inv.search(103))

inv.display_product_name()

#inv.display_all()
 
#inv.total_inventory_value()


class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance


    def deposit(self,amount):
        if amount>0:
            self.balance+=amount   

    def withdraw(self,amount):
        if self.balance>amount and (self.overdraft_limit==0 or self.overdraft_limit==None):
            self.balance-=amount
        elif amount>self.balance+self.overdraft_limit
            self.balance-=amount    

    def display(self):
        return f"AccountNo:{self.account_no} HolderName:{self.holder.name} Balance:{self.balance}"


class SavingAccount(BankAccount):
    def __init__(self,account_no,holder_name,balance,interest_rate)
        super().__init__(account_no,holder_name,balance)
        self.interest_rate=interest_rate


    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 

class CurrentAccount(BankAccount):
    def __init__(self,account_no,holder_name,balance,overdraft_limit)
        super().__init__(account_no,holder_name_balance)
        self.overdraft_limit=overdraft_limit        


class Bank:
    def __init__(self):
        self.Accounts={}


    def add_account(self,account):
        self.Accounts[account.account_no]=account

    def remove_account(self,account_no):
        if account_no in self.Accounts.keys():
            del self.Account[account_no]    

    def search_account(self,account_no):
        for key,value in self.Accounts.items():
            if key==account_no:
                print(key,value) 

    def display_all(self):
        for i in self.Accounts.values():
            i.display():

    def total_money(self):
        total=0
        for i in self.Accounts.values():
            total+=total+i.balance

        print("Total money of Bank: "+total)    


class Observer:
    def update(self, temp):
        pass

class Weather:
    def __init__(self):
        self.observer=[]
        self.temp=0

    def subscribe(self,obj):
        self.observer.append(obj)

    def unsubscribe(self,obj):
        self.observer.remove(obj)
    
    def notify(self,temp):
        for i in self.observer:
            i.update(temp)

    def update(self,temp):
        self.temp=temp 
        self.notify(self.temp)       

class Mobile:
    def update(self,temp):
        print(f"mobile update {temp}")



W=Weather()
M=Mobile()
W.subscribe(M)
W.update(30)

class Book:
    
    def __init__(self,book_name)
        self.book_name=book_name
        

class User:
    
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class Member(User):
    
    def return_book(User):
        pass

class Librarian(User):
    

    def borrow_book(self):
        pass

    def search_book(self)
        pass

class Library:

    def __init__(self):
        self.b=Book()
        self.m=Member()
     
    def due_date(self):
        pass

    def fine_calculation(self):
        pass  

x=5
print(eval("x+10"))
print(exec("x+10"))
print(x)

import ast
str="x = 10 + 20"
tree = ast.parse(str)

print(ast.dump(tree, indent=2))


import dis
def add():
    return 10 + 20

dis.dis(add)

x=[1,2,3]
y=x[:2]
z=x[2:]
print(y)
print(z)

class Employee:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def getsetname(self):  
        return self.__name

    @getsetname.setter
    def getsetname(self,name):
        self.__name=name    


E=Employee("mohit",21)
print(E.getsetname)
E.getsetname="raj"
print(E.getsetname)
E2=Employee("mohan",25)
print(E is E2)
print(E==E2)


def fact(n):
    if n==1:
        return 1   
    return n*fact(n-1)     


print(fact(3))


class NameDesc:

        def __get__(self,instance,owner):
            print("getting var name")
            return '__get__'

        def __set__(self,instance,value):
            print("setting var name")
            return '__set__'

        def __delete__(self,instance):
            print("deleting var") 
            return '__delete__'

class AgeDesc:

        def __get__(self,instance,owner):
            print("getting var Age")
            return '__get__'

        def __set__(self,instance,value):
            print("setting var Age")
            return '__set__'

        def __delete__(self,instance):
            print("deleting var Age") 
            return '__delete__'


class Employee:
    name=NameDesc()
    age=AgeDesc()
    def __init__(self,name,age):
        self.name='mohit'
        self.age=21



E=Employee("mohit",21)
print(E.age)
print(E.age)
E.age=21
del E.age
 
class Animal:
    def makesound(self):
        pass

class bird(Animal):
    def makesound(self):
        print("bird make sound")

class dog(Animal):
    def makesound(self):
        print("dog make sound"):

class fish(Animal):
    def makesound(self):
        print("error: fish cannot make sound")


class AnimalMakesound:
    def makesound(self):
        pass

class AnimalDontmakesound:
    def animalswim(self):
        pass


class Bird(AnimalMakessound):
    def makesound(print):
        print("bird make sound")

class Fish(AnimalDontmakesound):
    def animalswim(self):
        print("fish swim")

class Employee:
    def __init__(self,name):
        self.__name=name

    @property
    def getsetname(self):
        return self.__name
    @getsetname.setter
    def getsetname(self,name):
        self.__name=name
   

E=Employee("test")
E.getsetname="test2"
print(E.getsetname)
print(E._Employee__name)

print(type(E))
print(type(Employee))

"""
class Employee:
    pass


E=Employee()
"""
print(type(E))
print(type(Employee))
print(type(object))

print(isinstance(E,object))
print(isinstance(Employee,object))
print(isinstance(type,object))
print(isinstance(object,type))
print(isinstance(object,object))
print(isinstance(type,type))

#print(issubclass(E,object))
print(issubclass(Employee,object))
print(issubclass(type,object))
print(issubclass(object,type))
print(issubclass(object,object))
print(issubclass(type,type))
 

def logging(fun):
    def securitycheck():
        print("profile checking")
        fun()
        print("profile check completed")
    return securitycheck    

 
 

@logging
def profile():
    print("this is your profile info")

#profile=logging(profile)    

profile()

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage})"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

# Usage
 


pc=ComputerBuilder()
pc.set_cpu("Intel i7")
pc.set_ram("16GB")
pc.set_storage("1 TB SSD")
p=pc.build()
print(p)

#Builder pattern used composition
class Home:
    def __init__(self):
        self.solarPanel=None
        self.smartAppliances=None
        self.securityCamera=None
        self.RoomNumbers=None
        self.FloorsNumbers=None

    def __str__(self):
        return f"solarPanel:{self.solarPanel} |smartAppliances:{self.smartAppliances} | securityCamera:{self.securityCamera} |RoomNumbers:{self.RoomNumbers} |FloorsNumbers:{self.FloorsNumbers}"   

class HomeBuild:
    def __init__(self):
        self.MyHome=Home()

    def setup_solarPanel(self,flag):
        self.MyHome.solarPanel=flag
        return self

    def setup_smartAppliances(self,flag):
        self.MyHome.smartAppliances=flag
        return self

    def setup_securityCamera(self,flag):
        self.MyHome.securityCamera=flag
        return self

    def setup_RoomNumbers(self,roomnumbers):               
        self.MyHome.RoomNumbers=roomnumbers
        return self

    def setup_FloorNumbers(self,floornumbers):
        self.MyHome.FloorsNumbers=floornumbers
        return self

    def home_build(self):
        return self.MyHome       

H=HomeBuild()
MyHome=H.setup_solarPanel(True).setup_smartAppliances(True).setup_securityCamera(True).setup_RoomNumbers(3).setup_FloorNumbers(2).home_build()
print(MyHome)

#Adapter pattern
class Legacypayment:
    def LPayementsystem(self):
        print("processing Legacy payment")

class AdapterPayment:
    def __init__(self,lagacyObj):
        self.lagacyObj=lagacyObj

    def ProcessPayment(self):
        self.lagacyObj.LPayementsystem()

L=Legacypayment()
A=AdapterPayment(L)
A.ProcessPayment()
"""
from abc import ABC,abstractmethod
class Home(ABC):
    @abstractmethod
    def Addfloors(self):
        pass
    @abstractmethod
    def AddRooms(self):
        pass

class DesigneHome(Home):
    def Addfloors(self):
        return "Adding 2 floors"
    def AddRooms(self):
        return "Adding 2 Rooms"

class HomeDecoratorBase(Home):
    def __init__(self,obj):
        self.obj=obj

    def Addfloors(self):
        return self.obj.Addfloors()
    def AddRooms(self):
        return self.obj.AddRooms()

class FloorDecorator(HomeDecoratorBase):
    def Addfloors(self):
        return super().Addfloors()+"| Adding 2 more floor"

class RoomDecorator(HomeDecoratorBase):
    def AddRooms(self):
        return super().AddRooms()+"| Adding 2 more rooms"


D=DesigneHome()
F=FloorDecorator(D)
R=RoomDecorator(D)
print(F.Addfloors())
print(R.AddRooms())










    













 

 








