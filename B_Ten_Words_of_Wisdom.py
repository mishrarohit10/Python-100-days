
t = int(input())
for i in range(t):
    n = int(input())

    arr = []
    maxx = 0
    index = 0
    for i in range(n):
        a , b = map(int, input().split())
        arr.append(a)
        arr.append(b)

        if a <= 10:
            if b > maxx:
                maxx = b
                index = i
    
    print(index+1)


    
    
    



