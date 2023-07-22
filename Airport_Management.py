def maxPlatform(arrival, departure, n):
        m = {}
        for i in range(n):
            if arrival[i] not in m:
                m[arrival[i]] = 1
            else:
                m[arrival[i]] += 1
            if departure[i] not in m:
                m[departure[i]] = 1
            else:
                m[departure[i]] += 1
        return max(m.values())

t = int(input())
for i in range(t):
    n = int(input())
    arrival = list(map(int, input().split()))
    departure = list(map(int, input().split()))
    print(maxPlatform(arrival, departure, n))

    
