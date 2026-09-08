"""
# =========================================================
# input:AABCCDMMD
# output:AB
#        CD
#        MD
# =========================================================
def merge(str1,str2):
    for i in range(len(str1)):
        substring=str1[:i]+str1[i+1:]
        seen=""
        for char in substring:
            if char not in seen:
                seen+=char
        print(seen)
s=input("enter the string") 
k=int(input("enter string len"))      
merge(s,k)   

# =========================================================
# input:
# str1='mohit1'
# str2='mohit'
# output:5
# =========================================================

def findidx(str1,str2):
    for i in range(len(str1)):
        substring=str1[:i]+str1[i+1:]
        if substring==str2:
            print(i)

str1=input("enter the first string") 
str2=input("enter the second string")      
findidx(str1,str2)   

# =========================================================
#factorial with recursion
# input:5
# output:20
# =========================================================


n=0
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)    

print(fact(5))



# =========================================================
#accpeting multiple arguments without specifying no of arguments
# input:5
# output:20
# =========================================================



 

# **kwargs example
def fun(**kwargs):
    for k, val1 in kwargs.items():
        print(k, val1)
fun(a=1, b=2, c=3)
 
#range(start, stop) 
#range(start, stop, step)

--for printing number
n=int(input("enter a number"))
if n>=1 and n<=20:
        for i in range(n):
            print(i*i)

--for getting exponential of number
   a = int(input())
    b = int(input())
    if a>=1 and a<=10**10:
        print(a+b)
        print(a-b)
        print(a*b)

 //->floor division return whole no
 /->division return number including decimal       

#printing leap year
def is_leap(year):
    leap = False
    if year >=1900 and year<=10**5:
        if year/4==0: 
            leap = True
        elif year/100==0:
            leap = False
        elif year/400==0:
            leap= True     
    # Write your logic here   
    return leap

year = int(input())
print(is_leap(year))
   
n = int(input())
    for i in range(n):
        print(i)
 
# printing string in one line
n = int(input())
c=''
if(n<=150):
    for i in range(1,n+1):
            c=c+str(i)

    print(c)
 # range (5) will start from 0 and end at 4


n = int(input())
 
if(n<=150):
    for i in range(n5):
            print(i)

n=int(input())
sqr=[i * i for i in range(n)] 
print(sqr)  


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            ch=''
            i=0
            for c in s:
                if c not  in ch: 
                    ch=ch+c

            print(len(ch)) 
n=input()            
sol=Solution()   
sol.lengthOfLongestSubstring(n)   

def mergearr(arr1:[],arr2:[]):
    arr3=arr1+arr2
    x=0
    for i in arr3:
        x=x+i
    print(x/len(arr3))    
ar1=input()   
ar2=input() 
mergearr(ar1,ar2)  


# to get list input 
arr=list(map(int,input().split(",")))
print(arr)
print(len(arr))

#get input two array and calculate median
{1,2,3}->median is 2
{1,2,3,4}->median is (2+3)/2->2.5
class Solution:
    def findMedianSortedArrays(self, num1: list[int], num2: list[int]) -> float:
            num3=num1+num2
            lt=len(num3)
            rem=lt//2
            if lt%2==0:
                print((num3[lt/2]+num3[(lt/2)-1]/2))
            else:
                print(num3[lt//2])    

s=Solution()
ar1=list(map(int,input().split(',')))
ar2=list(map(int,input().split(',')))
s.findMedianSortedArrays(ar1,ar2)

arr=list(map(int,input().split(',')))
print(arr)

##switch case 
inp=input()
match inp:
    case 'x':
        print('matched x')
    case 'y':
        print('matched y')
    case 'z':
        print('match z')

import re as regexp
strinput=input('enter a string')
result=regexp.search(r"\d+",strinput)   
print(result.group())    


import re as regexp
strinput=input('enter a valid email')
if regexp.search(r".+@.+\.com",strinput):
    print('valid email')
else:
    print('invalid email')    

i, j, k = 1, 2, 3
print(i)
print(j)
print(k)



from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
            l=0
            r=len(height)-1
            #area=widhth*min(ht(0),ht(i-1))
            max_area=0
            while l<r:
                widhth=r-l
                ht=min(height[l],height[r])
                max_area=max(max_area,(widhth*ht))
                if(height[l]<height[r]):
                    l=l+1
                else:
                    r=r-1
            return max_area

arr1 = list(map(int, input().strip("[]").split(",")))

s = Solution()

print(s.maxArea(arr1)) 


#[1,2,3,4]
#l=0
#r=3

#3245

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = []

        for value, symbol in values:
            while int(num) >= value:
                result.append(symbol)
                num =int(num)-value

        return "".join(result)
s=Solution()
print(s.intToRoman(input()))        


"""







            


