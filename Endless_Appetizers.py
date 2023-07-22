t = int(input())
for i in range(t):
    x, y, r = map(int, input().split())

    e = (r//30) + x

    if e % y == 0:
        print(e//y)
    
    else:
        print((e//y) + 1)