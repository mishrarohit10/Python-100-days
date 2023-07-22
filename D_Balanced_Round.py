
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    index, res = 0, 0
    while index < n:
        right = index + 1
        
        while right < n:
            if arr[right] - arr[index] > k:
                break
            right += 1

        total = right - index
        res = max(res, total)
        index = right
    
    print(n - res)






