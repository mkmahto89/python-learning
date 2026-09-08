#Binary search 
"""
Conditions to apply Binary Search Algorithm in a Data Structure
The data structure must be sorted.

Access to any element of the data structure should take constant time.
Binary Search Algorithm
Divide the search space into two halves by finding the middle index "mid". 
Compare the middle of the search space with the key. 
If the key is found at middle, the process is terminated.
If the key is not found at middle, choose which half will be used as the next search space.
-> If the key is smaller than the middle, then the left side is used for next search.
-> If the key is larger than the middle, then the right side is used for next search.
This process is continued until the key is found or the total search space is exhausted.

Consider an array arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}, and the target = 23.
                           0  1  2   3   4   5  6   7    8  9

midvaleInd=(len(input_arr)/2)-1

if(input_arr[midvaleInd]=search_val)
    return 1
else:
    if search_val>input_arr[midvaleInd]
        midvaleInd=((midvaleInd+1)-len(midvaleInd)/2)-1



    if search_val<input_arr[midvaleInd]



 
def binary_search(input_arr,search_val):
    start_idx=0
    last_idx=len(input_arr)-1
    flag_found=0

    while  flag_found==0:
        mid_idx=(start_idx+last_idx)//2
        if(input_arr[mid_idx]==search_val):
            flag_found=1
        else:

            if start_idx+1==last_idx and (input_arr[start_idx]==search_val or input_arr[last_idx]==search_val):
                flag_found=1
                break 
            elif start_idx+1==last_idx:
                flag_found=-1
                break 
            elif search_val>input_arr[mid_idx]:
                start_idx=mid_idx

            elif search_val<input_arr[mid_idx]:
                last_idx=mid_idx
             

    return flag_found   



def binary_search_simple(input_arr,search_val):
    start_idx=0
    last_idx=len(input_arr)-1

    while  start_idx<=last_idx:
            mid_idx=(start_idx+last_idx)//2
            if(input_arr[mid_idx]==search_val):
                return mid_idx
            elif search_val>input_arr[mid_idx]:
                start_idx=mid_idx+1

            elif search_val<input_arr[mid_idx]:
                last_idx=mid_idx-1
             

    return -1  


#print(binary_search_simple([1,2,3,4,6,8,11,13,14,19],4) )  
#print(binary_search_simple([1,2,3,4,6,8,11,13,14,19],5) )
print(binary_search_simple([1,4,9],5) )



def merge(left,right):
    temp_arr=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp_arr.append(left[i])
            i+=1
        else:
            temp_arr.append(right[j])
            j+=1

    temp_arr.extend(left[i:])
    temp_arr.extend(right[j:])

    return temp_arr

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid_idx=len(arr)//2

    left=merge_sort(arr[:mid_idx])
    right=merge_sort(arr[mid_idx:])

    return merge(left,right)

print(merge_sort([4,3,2,1]))
#print(merge_sort([10,9,8,7,6,5,4,3,2,1]))

def binary_search(arr,search_val):

    mid_idx=(len(arr)//2)-1
    left=0
    right=len(arr)-1

    while left<=right:
        print(left,right)
        mid_idx=(left+right)//2
        if search_val==arr[mid_idx]:
            return mid_idx
        elif search_val>arr[mid_idx]:
            left=mid_idx+1
        elif search_val<arr[mid_idx]:
            right=mid_idx-1

    return -1


print(binary_search([1,2,3,4,5,6],7))   

 
#Knapsack problem
Given two arrays, val[] and wt[], where each element represents the value and weight of an item respectively, 
also given an integer W representing the maximum capacity of the knapsack (the total weight it can hold).
Put the items into the knapsack such that the sum of values associated with them is the maximum possible,
without exceeding the capacity W.

Note: We can either include an item completely or exclude it entirely - we cannot include a fraction of an item.

Examples:

Input:  W = 4, 
val[] = [1, 2, 3]
wt[] =  [4, 5, 1]
Output: 3
Explanation: There are two items with weight less than or equal to 4. If we select the item with weight 4,
 the possible value is 1, and if we select the item with weight 1, the possible value is 3. 
 Hence, the maximum possible value is 3. We cannot put both items with weights 4 and 1 together because
  the capacity of the bag is 4.

Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
Output: 0 
Explanation: All the item weights are greater than the knapsack capacity.
v= 1,2,3,3
w= 2,3,4,1

w=5


def Knapsack(val,wt,w):

    lst_wt=[]
    lst_val=[]
    for i in range(len(wt)):
        for j in range(i+1,len(wt)):
            if wt[i]+wt[j]<=w and sum(lst_val)<(val[i]+val[j]):
                lst_wt.clear()
                lst_val.clear()
                lst_wt.extend([wt[i],wt[j]])
                lst_val.extend([val[i],val[j]])

    return(lst_wt)            


print(Knapsack([1,2,3,3],[2,3,4,1],5))

print(Knapsack([1,2,3,3,3],[2,3,3,1,1],5))

 
v= 1,2,3,3,3
w= 2,3,3,1,1
w= 5
 

[ 
  [1,2,3,3,3],
  [2,3,3,1,1]
]
"""
#Dijkstra's Algorithm
"""
 if cur_dis>distance[cur_node]:
            continue

Why the continue is needed
The heap can contain multiple entries for the same node because every time a shorter path is found, you push a new (distance, node) pair.
For node B, the heap contained:
(4,B)   ← old
(3,B)   ← new shorter path
The heap pops (3,B) first, and distance[B] becomes 3. Later, (4,B) is popped, but it's no longer valid, so this check:
if cur_dis > distance[cur_node]:
    4>3
    continue
ignores it.



import heapq
def dijkstra(graph,start):
    distance={node:float('inf') for node in graph}
    distance[start]=0

    pq=[(0,start)]

    while pq:
        cur_dis,cur_node=heapq.heappop(pq)

        if cur_dis>distance[cur_node]:
            continue

        for neighbour,weight in graph.get(cur_node,[]):
            new_dis=weight+cur_dis

            if new_dis<distance[neighbour]:
                distance[neighbour]=new_dis

                heapq.heappush(pq,(new_dis,neighbour))

    return distance  
              
graph={
'A':[('B',4),('C',2)],
'B':[('A',4),('C',1),('D',5)],
'C':[('A',2),('B',1),('D',8),('E',10)],
'D':[('B',5),('C',8),('E',2)],
'E':[('C',10),('D',2)]
}
print(dijkstra(graph,'A')) 

#merge two sorted array


def mergearray(arr1,arr2):
    i=j=0
    ar=[]

    while len(arr1)>i and len(arr2)>j:
        if arr1[i]>arr2[j]:
            ar.append(arr2[j])
            j+=1
        else:
            ar.append(arr1[i])
            i+=1


    ar.extend(arr1[i:])
    ar.extend(arr2[j:])
    return ar

arr1=[1,5,9]
arr2=[2,4,8]
print(mergearray(arr1,arr2))
"""
#This code finds the maximum sum of any contiguous subarray of size k.
#arr = [5, 2, -1, 0, 3]
#k = 3

def findmaxsubarray(arr,k):
    max_sum=0
    cur_sum=0
    l=len(arr)

    for i in range(l-k+1):
        for j in range(k):
            cur_sum+=arr[i+j]

        max_sum=max(max_sum,cur_sum)    

    return max_sum   
    
arr = [5, 2, -1, 0, 3]
k = 3
print(findmaxsubarray(arr,k))




 
 





    

 


  


  


                

        
    


    