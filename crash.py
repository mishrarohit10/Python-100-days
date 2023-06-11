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


