t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    prefix = [0] * n

    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    prefix.sort(reverse=True)
    
    #print prefix as string with spaces
    print(' '.join(map(str, prefix)))