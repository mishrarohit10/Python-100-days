t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())

    if x * y % z == 0:
        print(x*y, end = " ")
        print(z)

    
    elif x * z % y == 0:
        print(x*z, end = " ")
        print(y)

    elif y * z % x == 0:
        print(y*z, end = " ")
        print(x)

    else:
        print(-1)