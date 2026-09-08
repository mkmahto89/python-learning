"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target.
You may assume that each input would have exactly one solution, and you may not use the same element
twice.
nums = [2,7,11,15]
target = 9

nums = [2,7,11,15]
        0 1 2 3
target = 9

start with 0,0+1=?
             0+2=?
             0+3=?

             1+2=?
             1+3=?

             2+3?


def GetIndex(InputArr,TargetNum):
    for i in range(len(InputArr)):
        for j in range(i+1,len(InputArr)):
            if TargetNum==(InputArr[i]+InputArr[j]):
                return [i, j]


print(GetIndex([2,7,11,15],9))
#time complexity->n*n->O(n^2)
#space compexity->
########################################################################################
Valid Word Square Problem (LeetCode 422)
A word square means:
Number of words = length of each word
The i-th row must be equal to the i-th column
Example:
Input:
[
 "ball",
 "area",
 "lead",
 "lady"
]
Visualize:
b a l l
a r e a
l e a d
l a d y
Rows:
ball
area
lead
lady
 
Arr=[]
lst=['']*8
for _ in range(4):
    Arr.append(input())


for i in range(4):
    for j in range(4):
        lst[i]+=Arr[i][j]

for i in range(4):
    for j in range(4):
        lst[i+4]+=Arr[j][i]     

print("printing answer")
for i in  range(len(lst)):
    for j in  range(i+1,len(lst)): 
                if lst[i]==lst[j] :
                    print(lst[i]) 
leetCode: 743 
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges
 times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal 
 to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.    

Input: times = [ [2,1,1]
                ,[2,3,1]
                ,[3,4,1]
                ], n = 4, k = 2
{
 2:[(1,1),(3,1)],
 3:[(4,1)]

}
{2: [(1, 1), (3, 1)],
 3: [(4, 1)]
}
Output: 2

import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        distance = {node: float('inf') for node in range(1, n + 1)}
        distance[k] = 0

        pq = [(0, k)]

        while pq:
            cur_dis, cur_node = heapq.heappop(pq)

            # Ignore old/worse distance
            if cur_dis > distance[cur_node]:
                continue

            for neighbour, weight in graph.get(cur_node, []):
                new_dis = cur_dis + weight

                if new_dis < distance[neighbour]:
                    distance[neighbour] = new_dis
                    heapq.heappush(pq, (new_dis, neighbour))

        max_time = max(distance.values())

        # If any node is unreachable
        if max_time == float('inf'):
            return -1

        return max_time

s=Solution()
input_mat = [[2,1,1],[2,3,1],[3,4,1]]
src_node = 2
node_no = 4

print(s.networkDelayTime(input_mat,node_no,src_node))

#replace vowel in the string 

def replacevowel(a):

    left=0
    right=len(a)-1
    vowellist=['a','e','i','o','u']
    while right>left:
            if a[left] in vowellist  and a[right] in vowellist:
                st=a[right]
                a[right]=a[left]
                a[left]=st
            right-=1
            left+=1

    return  a

print(['a','b','c','i','d','e'])
print(replacevowel(['a','b','c','i','d','e']))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


head=Node(1)
head.next=Node(2)
head.next.next=Node(3)

while head:
    print(head.data)
    head=head.next

#reverse a link list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def printnode(self,head):
        while head:
            print(head.data)
            head=head.next  
    def reverselinklist(self,head):
        cur_node=head
        prev=None
        while cur_node:
            nxt=cur_node.next
            cur_node.next=prev
            prev=cur_node
            cur_node=nxt

    def findingmiddleLinklist(self,head):
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow.data 


    def hascycle(self,head):
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast
                return True
            else:
                return False




N1=Node(1)
N1.next=Node(2)
N1.next.next=Node(3)

print(N1.printnode(N1))
print(N1.findingmiddleLinklist(N1))
nd=N1.reverselinklist(N1)
print(N1.printnode(nd))


deque methods are:
append() → add to right side
appendleft() → add to left side
pop() → remove right side
popleft() → remove left side


#Tree Traversal
#DFS--going level wise
from collections import deque
class TreeTravsal:

    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

    def preorder(self,root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def postorder(self,root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)

    def levelordertravesal(self,root):
        if not root:
            return

        queue=deque([root])
        while queue:
            node=queue.popleft():
            print(node.value,end=" ")
            if node.left:
                queue.append(node.left):
            if node.right:
                queue.append(node.right):
 
def fib(n):
    if n<=1:
        return  n
    return fib(n-1)+fib(n-2)


print(fib(6))
"""
 


                    



 









 
 
        