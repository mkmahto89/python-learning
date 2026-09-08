

"""
n = 3

matrixA = [[0 for j in range(n)] for i in range(n)]

print(matrixA)
print('-----')
n = 3

matrix3D = [[ [0 for k in range(n)] 
              for j in range(n)
            ]s
            for i in range(n)]

print(matrix3D) 

n=int(input("get no of rows needed"))

twoDArray=[[0 for k in range(n)] for i  in range(n)]
print(twoDArray)

three3DArray=[[[0 for i in range(n)] for j in range(n)] for k in range(n) ]
print(three3DArray)


for i in range(n):
    matrixA.append(int(input()))

matrixB=[]
for _ in range(n):
    matrixB.append(int(input()))

print(matrixA, matrixB)    

matrixC=[]
for i in range(len(matrixA)):
    for j in range(len(matrixB)):
        matrixC.append(int(matrixA[i])*int(matrixB[j]))

print(matrixC)   

 
00 01 02
10 11 12
20 21 22

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return self.x+other.x,self.y+other.y


V1=Vector(1,2)
V2=Vector(3,4)
V=V1+V2
print(V)


def myFun(fun):
    def wrapper():
        print("before")
        fun()
        print("after")
        print(type(wrapper))
    return wrapper #since this is belong to fun class

@myFun
def myf():
    print("in between")

myf()

def multiin(*a,**b):
    print(a[0],a[1],b["a"],b["c"])

multiin("a",1,a="wer",c="kjs")

import csv
with open("MyPython.csv","r" ) as f:
    red=csv.reader(f)
    for r in red:
        print(r)    


import pandas as pd
df=pd.read_csv("MyPython.csv")
print(df)
"""
"""
import pandas as pd
data={
"Name":["Mohit","Mohit_2","Mohit_3","Mohit_4","Mohit_5","Mohit_6"],
"Age":[21,22,23,24,25,26],
"Salary":[1000,2000,3000,4000,5000,6000],
"Department":["A","A","B","B","C","C"]
}
df=pd.DataFrame(data)
print(df.groupby("Department").max()["Salary"])
"""
"""
import pandas as pd


df=pd.read_excel("MyExcel.xlsx")

print(df)

result=df.groupby(["Department","Age"]).agg(
Minimum_Salary=("Salary","min"),
Maximum_Salary=("Salary","max")

)
#print(result)
#print(df.groupby(["Department"])["Salary"].max())
print(
df.groupby(["Department"]).agg(
MaxSal=("Salary","max")

)

)

print(
df.groupby(["Department"]).agg(
{
    "Salary":["min","max","count"]

}

)

)



mat=[[None]*3 for _  in  range(3)]
#print(mat)

print([None]*10)


1)== use to compare value 
2)is use to compare obj reference
3)if 1==1 give true , if obj1 is obj2 return false if both belong to different class instance
 
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

x=[[0 for _ in range(3)] for _ in range(4)]
print (x)


import re

x=re.match("hello","hello world")
x=re.search("hello","ink")
x=re.findall(r"\d","12232ssdsds")
print(x)

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def getsetname(self):
        return self.name,self.age    

    @getsetname.setter
    def getsetname(self,name):
        self.name=name

E=Employee('mohit',21)
print(E.getsetname)
E.name='karthik'
print(E.getsetname)

class MyClassMeta(type):

    def method1(cls):
        print("method1 print")

    def method2(cls):
        print("method2 print")

    def __new__(mtcs,obj,bases,namespace):

        namespace["var1"]="var1"
        namespace["var2"]="var2"
        namespace["method1"]=mtcs.method1
        namespace["method2"]=mtcs.method2
        return super().__new__(mtcs,obj,bases,namespace)  

class MyClass(metaclass=MyClassMeta):
    pass


M=MyClass()
(M.method1())            

class Employee:
    company="xyz"


E=Employee()
E.__class__.company="ABC"
print(E.company)

from dataclasses import dataclass
@dataclass
class Employee:
    age:int
    name:str


E=Employee(21,"myname")
print(E.name)


x= [[0 for _ in range(3)] for _ in range(3)]
print(x)
x.sort(key=lambda z:z[0])
print(list(x))

import re
print(re.match("search","search123"))  # check the string from start 
 

import heapq
def dijkstra(graph,start):


    distance={node:float('inf') for node in graph}
    distance[start]=0
    pq=[(0,start)]

    while pq:
        cur_dis,cur_node = heapq.heappop(pq)  #1-run A,0    

        if cur_dis>distance[cur_node]:   #1-run 0>0  A
            continue

        for neighbour,weight in graph.get(cur_node,[]):         #1-run B,4
                new_dis=weight+cur_dis                          #1-run 4+0
                if new_dis<distance[neighbour]:                 #1-run 4 < distance B   
                    distance[neighbour]=new_dis                 #1-run distance B =4 
                    heapq.heappush(pq,(new_dis,neighbour))      #1-run 4,B

    return distance    

graph={
'A':[('B',4),('C',2)],
'B':[('A',4),('C',1),('D',5)],
'C':[('A',2),('B',1),('D',8),('E',10)],
'D':[('B',5),('C',8),('E',2)],
'E':[('C',10),('D',2)]
}
#distance={'A':0,'B':'inf','C':'inf','D':'inf','E':'inf'}
#distance={'A':0,'B':1,'C':2,'D':3,'E':4}
print(dijkstra(graph,"A"))
 
class A:
    x = 10

a = A()
print(a.x)


 
class A:
    def __repr__(self):
        return "A Object"

a = A()
print(repr(a))

class A:
    pass

print(type(A))

dict1={"A":1,"B":2}
res=map(lambda x:x+"B",dict1)
print(dict(res))

filter(function, iterable)->return filter object so we need to convert into list
map(function, iterable)
Lambda:Creates a one-line function

lst=[1,2,3,4]
res=filter(lambda x:x%2==0,lst)
print(list(res))

res=list(map(lambda x:x*2,lst))
print(res)
"""
"""
sorted(iterable, key=function, reverse=False)
iterable → data you want to sort
key → function that extracts the sorting value
reverse → descending order if True
 
 

#Using list comprehension
#compare dictionary will compare both key and value
#" "
lst=[1,2,3,4,5,6,5]
lst=[x * x for x in lst]
lst=list(map(lambda x:x*x,lst))
print(lst)
res1=['A','B','C']
res="@".join(res1)
print(res)
Dictionary get() syntax:
dictionary.get(key, default_value)
result[key].append(word)
 
result = {
    "aet": ["eat", "tea"]
}


result["aet"].append("adb")
print(result)
 
dict1={}
st="leetcode"

for ch in st:
    dict1[ch]=dict1.get(ch,0)+1

print(min(dict1.items()))    
 
#Dynamic window problem
#longest subarray with sum <S

def longestsubarray(ar,s)->int:
    l,cur,best=-1,0,0
    for r in range(len(ar)):
        cur+=ar[r]
        while cur>=s:
            l+=1
            cur-=ar[l]
        best=max(best,r-l)
    return best


print(longestsubarray([4,5,2,0,1,8,12,3,6,9],15))

 
#two sum-->two pointers
def twosum(ar,target):
    l=0
    r=len(ar)-1
    while r>l:
        if ar[l]+ar[r]==target:
            return ar[l],ar[r]
        elif ar[l]+ar[r]>target:
            r-=1
        else:
            l+=1

print(twosum([-8,1,4,6,10,45],16))

#Input: s = "abcabcbb"
#Output: 3
#longest substring-->dynamic slinding window
def longestsubstring(s):
    l,r=-1,0,
    strdict={}
    for i,ch in enumerate(s):
        strdict[ch]=strdict.get(ch,0)+1
        r+=1
        while 
       

    return strdict

print(longestsubstring('abcabcbb'))   

import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right=len(nums)-1
        left=0
        org=copy.deepcopy(nums)
        nums.sort()
        while right>left:
            if nums[right]+nums[left]==target and nums[right]==nums[left]:
                return [left,right]
            elif nums[right]+nums[left]==target and nums[right]!=nums[left]: 
                return [org.index(nums[left]),org.index(nums[right])]
            elif nums[right]+nums[left]>target:
                right-=1
            else:
                left+=1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right=len(nums)-1
        left=0
        while right>left:
            if nums[right]+nums[left]==target:
                return [left,right]
            elif nums[right]+nums[left]>target:
                right-=1
            else:
                left+=1

st=set()
st.add(1)
print(st)    

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice=maxprice=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                print(prices[i],prices[j])
                if prices[j]>prices[i] and j>i:
                    minprice=min(minprice,prices[i])
                    maxprice=max(maxprice,prices[j])   

        return maxprice,minprice ,maxprice-minprice 


S=Solution()
print(S.maxProfit([7,1,5,3,6,4]))

 
def maxProfit(prices):
    buy=0
    sell=1
    profit=0

    while len(prices)>sell:
        if prices[sell]>prices[buy]:
            profit=max(profit,prices[sell]-prices[buy])
        else:
            buy=sell

        sell+=1
    return profit    

print(maxProfit([7,1,5,3,6,4]))  
 
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack=[]
        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)   # truncate toward zero

                stack.append(result)

        return stack[-1]


S=Solution()
#S.evalRPN(["2","1","+"])
print(S.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


def compress(chars: list[str]) -> int:
        lst=[]
        k=0
        for i in range(len(chars)):
            if chars[i] not in lst:
                lst.append(chars[i])
                k=1
                for j in range(i+1,len(chars)):
                    if chars[i]==chars[j]:
                        k+=1
                lst.append(k)        
        return lst

print(compress(["a","a","b","b","c","c","c"]))

class AdditionCls:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return AdditionCls(self.x+other.x,self.y+other.y)


A1=AdditionCls(2,3)
A2=AdditionCls(4,5)
A=A1+A2
print(A.x,A.y)   

from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    age:int


E=Employee("test",21)
print(E.name,E.age)

arr=[['mohit',21]
,['abc',22]
,['cyx',24]
]

x= [name,age for name,age in arr if age==21]
print(x)

a=[1,2,3,4,5]
del a[0]
a.remove(2)
a.pop()
a.pop(-1)
a.pop(0)
print(a)

##3 D matrix
mat_3d= [[[0 for _ in range(3)] for _ in range(3)]for _ in range(3)]
print(mat_3d)

mat_2D=[[0 for _ in range(3)] for _ in range(3)]
print(mat_2D)


import pandas as pd
data={
"name":["A","B","C","C"],
"age":[21,22,23,25],
"salary":[1000,2000,3000,40000]

}

df=pd.DataFrame(data)
print(df)

print(df.max(numeric_only=True))

print(df.groupby("name").max()["salary"])

print(df.groupby(["name"]).agg(
MinimumSalary=("salary","min"),
Maximumsalary=("salary","max")
)
)

class Employee:
    pass


E1=Employee()
E2=Employee()

E=Employee()

E1=E
E2=E

if E1 is E2:
    print(1)

if E1 == E2:
    print(1)
                


class MyError(Exception):
    pass

try:
    raise MyError("something went wrong...")
except MyError as e:
    print("error")
    print(e)

lst=[0]*5
print(lst)   

#dijkstra algo
import heapq

def dijkstra(graph,startnode):
    distance= {node:float('inf') for node in graph}
    distance[startnode]=0
    hpq=[(0,startnode)]
    while hpq:
        cur_dis,cur_node=heapq.heappop(hpq)
        if cur_dis>distance[cur_node]:
            continue 
        for neighbour,wt in graph[cur_node]:
            new_dis=wt+distance[cur_node]
            if new_dis<distance[neighbour]:
                distance[neighbour]=new_dis
                heapq.heappush(hpq,(new_dis,neighbour))

    return distance  

graph={
'A':[('B',4),('C',2)],
'B':[('A',4),('C',1),('D',5)],
'C':[('A',2),('B',1),('D',8),('E',10)],
'D':[('B',5),('C',8),('E',2)],
'E':[('C',10),('D',2)]
}
print(dijkstra(graph,'A'))

def sumarr(lst,k):

    max_sum=cur_sum=sum(lst[:k])
    for i in range(len(lst)-k):
        cur_sum+=-lst[i]+lst[i+k]
        max_sum=max(cur_sum,max_sum)

    return max_sum   

print(sumarr([1,2,3,-4,5,0],3))
 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
"""
Problem statement
You are given:
An array arr
A target value k
Find the length of the longest contiguous subarray whose sum is equal to k.
Example 1
arr = [1, 2, 3, 1, 1, 1, 1]
k = 6
Possible subarrays:
[1, 2, 3]       → sum = 6
[3, 1, 1, 1]    → sum = 6
[1, 1, 1, 1]    → sum = 4
The longest subarray is:
[3, 1, 1, 1]
Length:
4

def longestsubarraysum(lst,k):
    left=-1
    right=0
    sum_arr=0
    longest_len=0

    while left<len(arr)-1:
        for right in range(len(lst)):
            sum_arr=sum_arr+lst [right]+lst[left]
            if sum_arr==k:
                    longest_len=max(longest_len,right)
            elif sum_arr>k:





    while left<len(lst)-1:
            sum_arr=sum_arr+lst[right]
            right=right+1
             

##two sum brute
def twosum_brute(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return i,j             
print(twosum_brute([2, 7, 11, 15],9))

##two sum hash table
def twosum_hash(arr,target):
    seen={}
    for i,num in enumerate(arr):
        complement=target-num

        if complement in seen:
            return i,seen[complement]

        seen[num]=i  

print(twosum_hash([2, 7, 11, 15],9))

##two sum two pointers
def twosum_twopointers(arr,target):
    left=0
    right=len(arr)-1
    arr.sort()

    while left<right:
        if arr[left]+arr[right]==target:
            return left,right
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1 
print(twosum_twopointers([2, 7, 11, 15],9))  
 
Best Time to Buy and Sell Stock
Easy

Topics
conpanies icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to 
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

def buysellmax_brute(prices):
    max_profit=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]>prices[i]:
                max_profit=max(max_profit,prices[j]-prices[i])

    return max_profit

print(buysellmax_brute([7,1,5,3,6,4]))
print(buysellmax_brute([7,6,4,3,1]))

def buysellmax_pointer(prices):
    left=0
    right=1
    max_profit=0
    while right<len(prices):
        if prices[right]>prices[left]:
            max_profit=max(max_profit,prices[right]-prices[left])
            if right==len(prices)-1 and left==len(prices)-2:
                break
            elif right==len(prices)-1 and left<len(prices)-2:
                left+=1
            else:    
                right+=1
        elif prices[right]<prices[left]:
            left+=1
            right+=1

    return max_profit  

print(buysellmax_pointer([7,1,5,3,6,4]))
print(buysellmax_pointer([7,6,4,3,1]))
 
def buysellmax_pointer(prices):
    left=0
    right=1
    max_profit=0
    while right<len(prices):
        if prices[right]>prices[left]:
            max_profit=max(max_profit,prices[right]-prices[left])
        else:
            left=right

        right+=1

    return max_profit

print(buysellmax_pointer([7,1,5,3,6,4]))
print(buysellmax_pointer([7,6,4,3,1]))

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
def PolishnotationCalc(tokens):
    stk=[]

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stk.append(int(token))
        else:
            a=stk.pop()
            b=stk.pop()

            if token=="+":
                result=a+b 
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)  

            stk.append(result)   

    return stk[-1]         



print(PolishnotationCalc(["2","1","+","3","*"]))  
 
# [2,3,1,2,4,3]
# len->2
def minSubArrayLen_brute(target: int, nums: list[int]) -> int:
    minlen=float('inf')   
    
    for i in range(len(nums)):
        cur_sum=0
        for j in range(i,len(nums)):
            cur_sum+=nums[j]
            if cur_sum>=target:
                minlen=min(minlen,j-i+1)
                break

    return minlen        
    
 

print(minSubArrayLen_brute(7,[2,3,1,2,4,3]))
 
def minSubArrayLen_slindingwindow(target: int, nums: list[int]) -> int:

    minlen=float('inf')
    left=0
    cur_sum=0
    for right in range(len(nums)):
        cur_sum+=nums[right]
        while cur_sum>=target:
            minlen=min(minlen,right-left+1)
            cur_sum-=nums[left]
            left+=1

    return 0 if minlen==float('inf') else minlen  

print(minSubArrayLen_slindingwindow(7,[2,3,1,2,4,3]))
 
There are n people standing in a queue, and they numbered from 0 to n - 1 
in left to right order. You are given an array heights of distinct integers
 where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody 
in between is shorter than both of them. More formally, the ith person can 
see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people 
the ith person can see to their right in the queue.
 
def canSeePersonsCount(heights: list[int]) -> list[int]:
    lst=[0]*len(heights)
    right=0
    for left in range(len(heights)-1):
        cnt=0
        right=left+1 
        while heights[left]>heights[right]:
            cnt+=1
            lst[left]=cnt
            right+=1
            if right==len(heights):
                break 
            elif  heights[left]<=heights[right+1]:
                cnt+=1
                lst[left]=cnt
            cnt+=1

    return lst  

from collections import deque   
def canSeePersonsCount_queue(heights: list[int]) -> list[int]:
    q=deque(heights)
    lst=[0]*len(heights)
    j=0
    k=0
    while q:
        num=q.popleft()
        for i in range(1,len(heights)):
            j=j+1
            if num>heights[i]:
                lst[k]=j
            else:
                lst[k]=j
                break    
            print(lst)
        k+=1        
    return lst            


print(canSeePersonsCount_queue([10,6,8,5,11,9]))

def canSeePersonsCount_stack(heights: list[int]) -> list[int]:
    stk=[]
    l=len(heights)-1
    ans=[0]*len(heights)

    for i in range(l,-1,-1):
        cnt=0

        while stk and heights[i]>stk[-1]:
            stk.pop()
            cnt+=1

        if stk:
            cnt+=1

        ans[i]=cnt
        stk.append(heights[i])   

    return ans   

print(canSeePersonsCount_stack([10,6,8,5,11,9]))
 
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]


cnt=0
seeflag=0
10(0)
    seeflag=0
    10(0)>6(1)  
        if j-i>1
             if  lst[j-1]<lst[j]  then cnt+1 and seeflag=1
    
    if seeflag=1
        arr[i]=cnt+1
     else
        arr[i]=cnt

        
              


Input: heights = [10,6,8,5,11,9]
                   0,1,2,3,4,5
Output: [3,1,2,1,1,0]

def canSeePersonsCount_hash(heights: list[int]) -> list[int]:

    cnt=0
    seeflag=0
    dt=[0]*len(heights)
    lastflag=0

    for i in range(len(heights)):         
        cnt=0
        seeflag=0
        lastflag=0
        for j in range(i+1,len(heights)):                        
            if heights[i]>heights[j] and j-i>1:              
                if heights[j]>heights[j-1]:                                       
                    cnt+=1                                 
                    seeflag=1                              
            elif heights[i]>heights[j]:              
                cnt+=1   
            elif heights[i]<heights[j] and j-i==1:
                cnt+=1 
                lastflag=1 
                                       

            if seeflag==1:
                dt[i]=cnt+1
            else:
                dt[i]=cnt
    return dt   


print(canSeePersonsCount_hash([10,6,8,5,11,9]))
print(canSeePersonsCount_hash([5,1,2,3,10]))

 

class Employee:
    pass


E= Employee()
E1=Employee()
print(E==E1)
print(E is E1)
print(E)
print(E1)

class MyMeta(type):
    def __new__(msc,name,bases,namespace):
            if 'save' not in namespace:
                raise TypeError("class must implement save  method")
            return super().__new__(msc,name,bases,namespace)

class A(metaclass=MyMeta):
    pass

from dataclasses import dataclass
@dataclass
class Employee:
    name:str
    age:int


E=Employee(1.12,"test")  
print(E.name,E.age)  

def fun():
    yield 1
    yield 2
    yield 3

#g=fun()
#print(next(fun()))



 


def fun3():
   return(i for i in range(5))
   
g1=fun3()
print(next(g1))
print(next(g1))
print(next(g1))

mat_1D=[0]*3
mat_2D= [[0 for _ in range(3)] for _ in range(3)]
mat_3D= [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
print(mat_1D)
print(mat_2D)
print(mat_3D)

import sys

class Employee:
    pass
E=Employee()
print(sys.refrencecount(E) )

mat=[[2,1,1],
     [2,3,1],
     [3,4,1]]


for u,v,w in mat:
    print(u,v,w)
 
lst=['a','b','c']

print(''.join(lst))

user=UserRepository()
ServiceLayer=ServiceLayer(user)

--repo
class UserRepository:
    def __init__(self):
        self.users=[]

    def create(self,user):
        self.users.append(user)
--srv
class ServiceLayer:
    def __init__(self,userrepo):
        self.userrepo=userrepo


def create(self,users):
    if len(user)<0:
        return
    return self.userrepo.create(users)  

 
class Customer:
    def __init__(self,name,phoneno,address):
        self.name=name
        self.phoneno=phoneno
        self.address=address

    def customer_cart(self,cart):
        self.cart=cart()

    def customer_buy_product(self,product):
        self.product=product    

class Product:
    def __init__(self,product_id,product_name,product_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_price=product_price

class Cart:
    def __init__(self,cartitems):
        self.cart_id=random.int()
        self.cartitems=cartitems

class CartItem:
    def __init__(self):
        self.products={}     

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCard(Payment):
    def process_payment(self):
        print("process payment via credit card")

class Paypal(Payment):
    def process_payment(self):
        print("process payment via paypal")

class UPI(Payment):
    def process_payment(self):
        print("process payment via UPI") 

class Discount(ABC):
    def process_discount(self):
        pass

class Regular(Discount):
    def process_discount(self):
        print("process discount Regular")

class Premium(Discount):
    def process_discount(self):
        print("process discount for premium")        

class Festival(Discount):
    def process_discount(self):
        print("process dicsount for Festival")


class PaymentType:
    @staticmethod
    def GetPayment(paymemttype):
        if paymenttype=="CreditCard":
            return CreditCard()
        elif paymenttype=="Paypal"
            return Paypal()
        elif paymenttype=="UPI":
            return UPI()


C=Customer("Mohit",98877777,"myaddress"):
P=Product(123321,"Product_1",1000):
   
a=[1,2,3]
b=a[::-1]
c=123
c=str(c)
print(b,c[::-1])
 
def revse(x)->int:
    sg=1
    if x<0:
        sg=-1

    reverse=0
    x=abs(x)
    while x>0:
        digit=x%10
        reverse=reverse*10+digit
        x=x//10

    #print(reverse)
    return 0 if reverse*sg>(2**23)-1 or reverse*sg<(-2**31) else reverse  

 
print(revse(1534236469))
print(revse(1534236469))

print((2**23)-1)

def longestConsecutive(nums: list[int]) -> int:
        
    nums.sort()

    print(nums)
 
    left=0
    count=0
    while left<len(nums)-1:
        if nums[left]+1==nums[left+1]:
            if count==0:
                count=2
            else:    
                count+=1
        left+=1        

    return count   

print(longestConsecutive([100,4,200,1,3,2]) )    

my_list = [1, 2, 3]

my_list. 
"""
ar_1d=[0]*3
ar_2d=[[0 for _ in range(3)] for _ in range(3)]
"""
ar_3d= [[[0] for _ in range(3) for in range(3)] for in range(3)]

print(ar_1d)
print(ar_2d)

print(ar_1d)
print(ar_2d)

import sys 
class Employee:
    def __init__(self,a,b):
        self.a=a
        self.b=b

E=Employee(1,2)
print(sys.getrefcount(E))

import threading
def multi_1():
    print("multi_1")

def multi_2():
    print("multi_2")

t1=threading.Thread(target=multi_1)
t2=threading.Thread(target=multi_2)
t1.start()
t2.start()
t1.join()
t2.join()


import multiprocessing
def task_1():
    print("task1")

def task_2():
    print("task2")

if __name__=="__main__":
    t1=multiprocessing.Process(target=task_1)
    t2=multiprocessing.Process(target=task_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
 
#validate phone
import re    
n=input("enter you phone no")
if re.fullmatch("\d{10}",n):
    print("its matched")
else:
    print("not matched")   
 
# Email validation

rex=r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
rex=r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"

import pandas as pd
data={
"name":["Mohit","Karthik","Raj","Sanmati"],
"Salary":[1000,2000,3000,4000],
"Age":[20,21,22,23],
"Department":["IT","IT","SEC","HR"]
}
df=pd.DataFrame(data)
print(df.count())
print(df.groupby("Department").agg(
MinimumSalary=("Salary","min"),
MaximumSalary=("Salary","max")

) )
 
class Employee:
    pass


E=Employee()
E2=E

if E is E2:
    print("is called")
if E == E2:
    print("== called")    

if isinstance(E,Employee):
    print("tt")
  
class MyMeta(type):

    def __new__(cls, name, bases, namespace):
        print("Class name:", name)
  

        return super().__new__(cls, name, bases, nam    espace)


class Employee(metaclass=MyMeta):
    pass
 
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

E=Employee("A",21)
print(E.__dict__)
print(E.__dict__.get("name","xx"))
print(E.__dict__.get("name1","xx"))
 
from dataclasses import dataclass

class ReqDesc:
    def __set_name__(self,owner,name):
        self.name=name

    def __set__(self,instance,value):
        if len(str(value))<=2:
                print("value length is less")
                return
        instance.__dict__[self.name]=value

    def __get__(self,instance,owner):
        print(f"{self.name} will give value")
        return instance.__dict__.get(self.name)            

@dataclass
class Employee:
    name=ReqDesc()
    age=ReqDesc()
    name:str
    age:int

E=Employee("n",21)    


class PositiveSalary:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Setting salary")

        if value < 0:
            raise ValueError("Salary cannot be negative")
        instance.__dict__[self.name] = value


class EmployeeMeta(type):
    def __new__(cls, name, bases, namespace):
        print(f"Creating {name}")

        if "salary" not in namespace:
            namespace["salary"] = PositiveSalary()
        return super().__new__(cls, name, bases, namespace)


class Employee(metaclass=EmployeeMeta):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, salary, bonus):
        self.bonus = bonus
        super().__init__(salary)

    def get_salary(self):
        return super().get_salary() + self.bonus


e = Employee(100000)
m = Manager(100000, 50000)

print("Employee salary:", e.get_salary())
print("Manager salary:", m.get_salary())

lst=[1,2,3,4,5,6,7,8,9]
lst2=['a','b','c','d']
res2=zip(lst,lst2)
print(res2)



res = [n for n in lst if n%2==0]
print(res)
res2=zip(lst,lst2)

print(set(res2))

def fn(*a,**b):
    print(a[0],a[1],a[2],b['a'],b['c'])


fn('a',2,3,a=1,c=3)

lst=[1,2,3,4]
res=iter(lst)
print(next(res))
print(next(res))

lst=['1','2','3']
print(lst)
print(list(map(int,lst)))   

from functools import reduce
lst=[1,2,3]
print(reduce(lambda x,y:x+y,lst))


def dec(f):
    def dwrapper(a,b):

        print("before")
        f(a,b)
        print("after")
    return dwrapper

@dec
def sum(a,b):
    return print(a+b)

sum(1,2)

def process_chunk(lst,chk_size):
    chk=[]
    for l in lst:
        chk.append(l)
        if len(chk)==3:
            yield chk
            chk=[]
    if chk:
        yield chk

for c in process_chunk([1,2,3,4,5,6,7,8,9,1,2,3,4,5],3):
    print(c)

#DIP

from abc import ABC,abstractmethod

class Salary(ABC):
    @abstractmethod
    def CalcSal():
        pass

class EmployeeSalary(Salary):
    def __init__(self,MonthlySal):
        self.MonthlySal=MonthlySal

    def CalcSal(self):
        return self.MonthlySal*12+1000

class PresidentSalary(Salary):
    def __init__(self,MonthlySal):
        self.MonthlySal=MonthlySal

    def CalcSal(self):
        return self.MonthlySal*12+2000


class MySal:
    def __init__(self,SalObj):
        self.SalObj=SalObj

    def ProcessSal(self):
        return self.SalObj.CalcSal()    


E=EmployeeSalary(1000)
M=MySal(E)
print(M.ProcessSal())
"""
#flattened list
# 

def flatlist(lst):
    for itm in lst:
        if isinstance(itm, list):
            yield from flatlist(itm)
        else:
            yield itm

l=[1, [2, [3, 4], 5], 6]
mylst=[]
for i in flatlist(l):
    mylst.append(i)

print(mylst)







    










        

 




    
 








    


                










                        

        

                



 









 






