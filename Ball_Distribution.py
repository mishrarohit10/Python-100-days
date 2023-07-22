t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sum = 0
    for i in arr:
        sum += i
    
    if sum <= n * (m - 1):
        print(0)
    else:
        print(sum - n * (m - 1))