list = [1,2,3,4,5]
list.append(0)
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list.index(1))
m = list.copy()
m[0] = 0 
print(list.count(1)) 
list.insert(1,544)
print(list)
list.extend(m)
print(list)
k = list + m
print(k)