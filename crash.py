# Variables are dynamically typed 
n = 0
print('n',n)

# Type is decided at runtime

n = 'abc'
print('n',n)

# Multiple assignments
n,m = 0, 'abc'

# Increment 
n = n + 1  #good
n += 1     #good
# n++    bad

# None is null (absence of value)
n = 4
n = None
print('n =',n)

# If statements dont need parentheses or curly braces
n = 1
if n < 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multiline conditions.
# and = && 
# or = ||

n,m = 1,2
if ((n > 2 and n !=m) or n == m ):
    n += 1

# while loops are similar 
n = 0
while n < 5:
    print(n)
    n += 1

# for loops from i = 0 to i = 4
for i in range(5):
    print(i)

# for loops from i = 2 to 5
for i in range(2,6):
    print(i)

for i in range(5,2,-1):
    print(i)

#  Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFULL: most languages round towards 0 
# by default so negative numbers will round down 
print(-3 // 2)

# A workaround for rounding towards zero is 
# use decimal division AND THEN CONVERT IT TO INT
print(int(-3/2))

# Modding is similar to most languages
print(10 & 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo 
import math 
print(math.fmod(-10,3))

# math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max / Min int 
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2,200) < float("inf"))

# Arrays (are called lists in python)
# dynamic by default
arr = [1,2,3]    

# Can be used as a stack
arr.append(4)
print(arr)
arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful -1 is not out of bounds
# its last value
# -2 is second last
arr = [1,2,3]
print(arr[-1])

# Sublists (aka string slicing)
# Similar to for-loops, last index is non inclusive
arr =[1,2,3,4]
print(arr[1:3])

# Unpacking 
a, b, c = [1,2,3]
print(a,b,c)

# Lopp through arrays

nums = [1 ,2 ,3]

# Using index 
for i in range(len(nums)):
    print(nums[i])


# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)
print("---------------------------")

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1, n2 in zip(nums1,nums2):
    print(n1, n2)
print("------------------------")

# Reverse and Sort
arr = [1,2,3]
arr.reverse()
print(arr)

# by default asc 
arr.sort()
print(arr)

# rerverse order (des)
arr.sort(reverse=True)

# Sorting strings
arr = ['bob', 'alice', 'charlie', 'jane', 'doe']
arr.sort()
print(arr)

# Custom sorting by length of the string
arr = ['bob', 'alice', 'charlie', 'jane', 'doe']
arr.sort(key=lambda x: len(x))
print("--------List Comprehension----------------")

# List comprehension
arr = [i for i in range(5)]
print(arr)
print("-----------------------")

# 2-D lists
arr = [[0]*4 for i in range(4)]
print(arr)

# This wont work
# each of thw four rows will be same if
# we modify one row others will also change
arr = [[0] * 4] * 4
print(arr)
arr[0][0] = 1
print(arr)
print("----------------------")

#  String 
s = "abc"
print(s[0:2])

# they are immutable
# s[0] = "A "
# print(s)

# this crteates a new string
s += 'xyz'
print(s)

# Valid numeric string are converted
print(int("123") + int('123'))
print(str(123) + str(123))

# ASCII values of char
print(ord('a'))
print(ord('b'))

# Combining a list of strings (which an empty string delimitor)

Strings = ['abe','efg','hijk']
print("-->".join(Strings))

# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)
print("-------------------------")

# Hash Set
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)

print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# list to set

print(set([1,2,3,4,5]))

# set comprehension
mySet = {i+1 for i in range(5)}
print(mySet)

# hashmap (aka dict)
myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77
print(myMap)
print(len(myMap)) # number of keys

myMap['alice'] = 80
print(myMap['alice'])

print('alice' in myMap)
myMap.pop('alice') #removing key will also remove the value
print('alice' in myMap)

myMap = {"alice": 90, "bob": 70}
print(myMap)

# Dict comprehension
myMap = {i: i*2 for i in range(3)}
print(myMap)

# Looping through dict
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key,myMap[key])

for val in myMap.values():
    print(val)

for key, value in myMap.items():
    print(key,value)

# Tuples are like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

# cant modify
# tup[0]=1

# can be used as key for hash map/set
myMap = {(1,2):3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# lists cant be keys
# myMap = [[3,4]] = 5

# Heaps 
import heapq
# by default minHeap
# under the hood are arrays
minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default , workaround is 
# to use min heap and * -1 when push and pop

maxHeap = []
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-1)

# max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# build heap from initial values
arr = [1,2,3,4,5,6,7]
heapq.heapify(arr)
while len(arr):
    print(heapq.heappop(arr))

# functions
def myfun(n, m):
    return n*n

# Nested functions have access to outer varialbes

def outer(a,b):
    c = 'c'

    def inner():
        return a + b + c
    return inner()
print(outer("a","b"))

# 



# classes
class MyClass:
    # constructor
    def __init__(self,nums):
        # member variables
        self.nums = nums

    # self key word is req as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getDoubleLength()
