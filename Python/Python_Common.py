"""
# try except finally
def trycatchtest():
    try:
        print(1/0)
    except:
        print('catch error')  
    finally:
        print('finally')      

trycatchtest()  


#list ,mutable 
print('--------list---------------')
lst=['a','c','b',1]   #list
print(lst)            #printing list
print(lst[0])         #get first elements of the list
for a in lst:         #printing all list data
    print(a) 


print('--------Set---------------')
#Set mutable 
st={'a','b',1,'a','b'}
#print(st[0]) #not allowed since its not index based
print(st)   #remove deplicate from the collection
for a in st:
    print(a)

print('---------tuple-------------')
#tuple ,immutable means it cannot be changed later 
tp=(1,2,3,4,5,1)
print(tp)
for a in tp:
    print(a)


import json 
print('--------dictonary-----------')
#dictinary

dict={"Name":"Mohit","Age":20,"Salary":1000}
print(dict)
js=json.dumps(dict)   # to convert into json
print(type(dict))
print(type(js))


js='{"Name":"Mohit","Age":20,"Salary":1000}'
print(js)
print(type(js))
dc=json.loads(js)    #to  convert into  dictionary
print(type(dc))
"""
#print(1==1)
#print(1 is 1)
#print('a' is 'a')
#print([]==1)
#print(0.2+0.3==0.5)
#print( 1 is True) #is operator is memory address chk operator
#cannot modify tuple
#a=(1,2,3)
#a[0]=2
#empty string is false
#bool(non empty string is true
#print(bool(""))  #false
#print(bool("ad")) #true
#print(bool("False"))
#print(bool("false"))
#print(bool(0))
#print(bool("1"))

#print("mohit's")
"""
lst=[[1,2,3]  #index 0
    ,[4,5,6]  #index 1
    ,[7,8,9]  #index 2
]

lst.append([1,2])
lst.remove([7,8,9])

print(lst[0][1])
print(lst[1][1])

for l in lst:
    for l1 in l:
            print(l1) 

l=[1,2,3,4,5]
 
print(l[:2])  #slicing getting all first two elements 
print(l[2:])  

print(l[:2]) means print(l[0:2])-- starting from 0 and stopping before 2

response = {
    "users": [-->index we need to use since its 
        {
            "id": 1,
            "name": "John",
            "addresses": [
                {"city": "Toronto"},
                {"city": "Brampton"}
            ]
        }
    ]
}
#Get "Brampton":

print(response['users'][0]['addresses'][1]['city'])

import json
import requests

js=requests.get('http://api.weather.com/v1')


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
  
st=''
for i in range(0,m):
        for j in range(0,n):
            st=st+matrix[j][i]


print(st)
    
 
import re
print(re.match(r"abc", "abcdef"))  # match -> it match from start of string 
print(re.match(r"abc", "zabc"))     # no match

if re.match(r"abc", "abcdef"):
    print("g")

if re.search(r"abc", "abcdef"):  # it will search from in all string 
    print("g")

print(re.findall(r"\d+","absg134"))   

print(re.sub(r"\d","#","abc123"))

print(re.split(r"\d","a1b555c6"))

print(re.split(r"\d+","a1b555c6"))


print(re.split(r"\d+","abc14gdj"))
print(re.split(r"\d","abc14gdj"))


import re
print(re.sub(r"\D+","#","ABC11124FDFD"))
print(re.sub(r"\D","@","KJSAKJBD12232SLFSHL"))
print(re.sub(r"\d+","$","123abc123"))
print(re.sub(r"\d+","!","123abc"))

m=re.search(r"(\d+)-(\d+)","123-456")
print(m.group(1))
print(m.group(2))

def main():
        ans="true"
        it=1
        temp=0
        mass=int(input())
        asteroids= list(map(int, input().split()))
        if(mass>=1 and mass<=10**5 and len(asteroids)<=10*5):
            for j in asteroids:
                if(j>=1 and j<=10**5):
                    continue
                else:
                    it=0    


        if(it==1):    
            for i in asteroids:
                if mass>=i:
                     mass=mass+i
                else:
                    ans="false"

        return ans

print(main())
 
class Employee:
    def __init__(self,name):
        self.name=name

    def Pr(self):
        print(f"name is :{name}")

E=Employee("mohit")
print(E)
#print(dir(E))
print(E.__class__.__dict__)
print(E.__class__.__bases__)
print(type("y"))  #str
print(type(int))   #type
print(type(type))  #type
print(type(object)) #type


dict={"nda":"national defecnce acedemy","ima":"india military academy"} 
#print(dict["nda"])     
for i in dict:
    print(i)

dict["afa"]="airforce academy"

for i in dict:
    print(f"{i} :{dict[i]}")

print(dict.get("afa"))

import requests
import json
response=requests.get("https://api.github.com/users/hadley/orgs")
response_json=response.json()
for i in response_json:
    print(response_json[i])

class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock

    def update_price(self,price):
        self.price=price

    def add_stock(self,quanity):
        self.stock+=quantity     

    def remove_stock(self,quantity):
        if self.stock>quantity:
            self.stock-=quantity
        else:
            print("Insufficient stock")    

    def display(self):
        print(f"Product ID:{self.product_id} Name:{self.name} Price:{self.price} Stock:{self.stock}")   

class Inventory:
    def __init__(self):
        self.Products={}

    def add_product(self,Prod):
        self.Products.append["product_id"]=Prod


p1 = Product(101, "Laptop", 50000, 5)
#p2 = Product(102, "Mouse", 500, 20)

inv = Inventory()

inv.add_product(p1)


def validation(func):

    def wrapper():
        print("pre validation")
        func()
        print("post validation completed")
    return wrapper    



@validation
def login():
    print("login successfull")


login()
"""
#generators
"""
def genfunc():
    yield 1
    yield 2
    yield 100

y=genfunc()   

print(next(y))
print(next(y))
print(next(y))


for x in y:
    print(x)

def func():
    return (i for i in range(10))


g=func()

print(next(g))
print(next(g))
print(next(g))


def fun():
    return (i for i in range(5))

g=fun()

for j in g:
    print(j)

def f():
    yield from range(3)

g = f()

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # StopIteration


def funGen():
    return (i for i in range(5))

def funGen_2():
    r = yield from funGen()

g = funGen_2()
#print(list(g))
print(next(g))

def arry():
    arr = [[0 for _ in range(3)] for _ in range(3) ]
    arr1 = [0 for _ in range(3)] 

    print(arr)
    print(arr1)


arry()

if __name__ == '__main__':
    
    name_lst=[]
    score_lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_lst.append(name)
        score_lst.append(score)
    
    arr=[[0 for _ in range(len(name_lst))] for _ in range(len(name_lst))]
    
    k=0
    for i in range(len(name_lst)):
        k=0
        arr[i][k]=name_lst[i]
        arr[i][k+1]=score_lst[i]
        
    score_lst.sort()
    st=set(score_lst)
    j=1
    scr=0
    
    for i in st:
        if j==2:
            scr=i
            break
        else:
            j+=1
            continue
            
    nm=[]
    l=0        
    for i in range(len(arr)):
        l=0
        if arr[i][l+1]==scr:
            nm.append(arr[i][l])
        else:
            continue                 
    
    nm.sort()    
    for i in nm:
        print(i)  


def fun(*args_1,**kwgrs_1):
    print(args_1[0],args_1[1],kwgrs_1['a1'],kwgrs_1['b'])


fun("a","b",a1="abc",b="skhdbs")

import requests
try:
    arr=[1,7,3,56,64,0]
    print(arr.sort())  #it will return None
    print(arr)

    arr_2d=[[9,2,1,0],[9,7,2,3]]
    arr_2d.sort(key=lambda x:x[1])
    #print(1/0)
    res=requests.get("http://google1.com")
    print(res)
  
except Exception as e:
    print("error 123",e)  
finally:
    print("final")  

class Employee:
    y=10
    def __init__(self,x):
        self.x=x

    def __call__(self):
        print(self.x)  

    @classmethod
    def funcl(cls,self):
        return cls.y,self.x      


e=Employee(123)
#print(e())
print(Employee.funcl(e))
e.__class__.y=129
Employee.y=123333
print(Employee.funcl(e))

#duck typing

class VSCode:
    def execute(self):
        print("executing in VS Code")

class PyCharm:
    def execute(self):
        print("executing in PyCharm")

class RunMethod:
    def rnmethod(self,obj):
        obj.execute()


V=VSCode()
P=PyCharm()

R=RunMethod()
R.rnmethod(V)

#meta

class A(type):
    
    def printname(self):
        return print("i am metaclass")
    def __new__(mcs,obj,bases,namespace):
        namespace["name"]="meta"
        namespace["printname"]=mcs.printname
        return super().__new__(mcs,obj,bases,namespace)

class Employee(metaclass=A):
    pass

E=Employee()
print(E.name)
print(E.printname())

class Solution:
    def longestPalindrome(self, s: str) -> str:
lst=[]
instr=[]
def IsPallindrone(str1):

    l=len(str1)
    revstr1=[]
    for i in range(l-1,-1,-1):
        (revstr1.append(str1[i]))

    if revstr1==str1:
        if len(str1)>len(lst):
            #print("pallin"+str(str1))
            del lst[:]
            lst.append(str1.copy())
         
      

def StrProcess():
    instr=input("enter a string\n")
    instr=list(instr)
    instrlst=[]     
    for i in range(len(instr)):
          instrlst.append(instr[i])
          for j in range(i+1,len(instr),1):
                #print(instrlst)
                instrlst.append(instr[j])
                IsPallindrone(instrlst)
          instrlst=[]        

 
del lst[:]
StrProcess() 
print(lst)     

class Solution:
    lst=[]
    instr=[]
    def longestPalindrome(self, s: str) -> str:
            instr=list(s)
            instrlst=[]     
            fin=''
            for i in range(len(instr)):
                instrlst.append(instr[i])
                for j in range(i+1,len(instr),1):
                        instrlst.append(instr[j])
                        self.IsPallindrone(instrlst)
                instrlst=[]  
            self.fin=''.join(self.lst)  
            return (self.fin)   

    def IsPallindrone(self,str1):

        l=len(str1)
        revstr1=[]
        for i in range(l-1,-1,-1):
            (revstr1.append(str1[i]))

        if revstr1==str1:
            if len(str1)>len(self.lst):
                #print("pallin"+str(str1))
                self.lst.clear()
                self.lst.extend(str1)          

c=Solution()
instr1=input("enter a string\n")
print(str(c.longestPalindrome(instr1)))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        OpenC=0
        CloseC=0
        Itg=0
        if len(s)>=0 and len(s)<=3*(10**4):
            for i in s:
                if i==')' or i=='(':
                    if i==')':
                        OpenC+=1
                    elif i=='(' :
                        CloseC+=1      
            if OpenC>CloseC and OpenC>0 and CloseC>0:
                Itg=CloseC
            elif OpenC<CloseC and OpenC>0 and CloseC>0:
                Itg=OpenC
            elif OpenC==CloseC:
                Itg=OpenC  

        return Itg*2

S=Solution()
print(S.longestValidParentheses(input()))

# list support stack
stk=[]
stk.append(1)
stk.append(2)
print(stk)
stk.pop()
print(stk)
print(stk[-1])
stk.clear()
print(stk)

import threading
import time

def Filedownload():
    print("downloading....")
    time.sleep(1)

def FileUpload():
    print("uploading......")
    time.sleep(1)

def ReadingFile():
    print("reading file....")
    time.sleep(1)        



t1=threading.Thread(target=Filedownload)
t2=threading.Thread(target=FileUpload)
t3=threading.Thread(target=ReadingFile)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Finish")

import multiprocessing
import time

def Filedownload_p():
    print("downloading....")
    time.sleep(1)

def FileUpload_p():
    print("uploading......")
    time.sleep(1)

def ReadingFile_p():
    print("reading file....")
    time.sleep(1)        


if __name__ == "__main__":
    t11=multiprocessing.Process(target=Filedownload_p)
    t21=multiprocessing.Process(target=FileUpload_p)
    t31=multiprocessing.Process(target=ReadingFile_p)

    t11.start()
    t21.start()
    t31.start()

    t11.join()
    t21.join()
    t31.join()

    print("Finish")

#fibonici series
first=0
second=1
for i in range(10):
    print(first)  
    next=first+second
    first=second
    second=next

#check no if armsstrong or not
num=(input("input a number"))
n=0
l=len((num))
for i in num:
    n+=(int(i)**l)

if(int(n)==int(num)):
    print("yes")
else:
    print("No")  

#febonici using recusrion

first=0
second=1
def feb(n)
    print(first)
    next=first+second
    first=second
    second=next


def fact(n):
    if n==1:
        return 1   #here it will stop since its not finding 
    return n*fact(n-1)     


print(fact(3))

def fibo(first,second,n):
    
    if n==0:
        return 
    next=first+second
    print(first)
    first=second
    second=next
    fibo(first,second,n-1)

fibo(0,1,10)
"""

    



          







