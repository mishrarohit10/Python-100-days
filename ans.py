
a , b , x , y = map(int,input().split())
messi = a * 2 + b
ronaldo = x * 2 + y
if messi > ronaldo:
    print("messi")
elif messi < ronaldo:
    print("ronaldo")
else:
    print("equal")