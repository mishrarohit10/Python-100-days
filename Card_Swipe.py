t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    maxsum = 0

    # create a set to store the unique elements
    s = set()

    # traverse the array
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
            sum += 1
            maxsum = max(maxsum, sum)
        else:
            #remove element from set
            s.remove(arr[i])
            sum -= 1
    print(maxsum)