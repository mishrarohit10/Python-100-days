l = [3,4,5]
print(l)
print(type(l))
print(l[0])
print(l[-2])
print(l[len(l)-2])

if "4" in l:
  print("yes")
else:
  print("no")

print(l)   
print(l[:])
print(l[1:4:2])

list = []
list = [i for i in range(1,6)]
print(list)