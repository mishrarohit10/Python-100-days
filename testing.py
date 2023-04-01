import math

# rough
testCases = int(input())
while testCases > 0:
    n = int(input())
    res = int(math.sqrt(n-1))
    print(res)
    testCases -= 1
