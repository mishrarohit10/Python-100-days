t = int(input())
for _ in range(t):
    b, c, h = map(int, input().split())

    sandwich = 0
    if b - 1 > c + h:
        sandwich = c + h + (c + h) + 1
        print(sandwich)
    
    else:
        print(2*b - 1)
        