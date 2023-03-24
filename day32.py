s1 = {1,2,3,4}
s2 = {2,3,4,5,8}
print(s1.union(s2))
s1.update(s2)
print(s1)
print(s2)
print(s1,s2)
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
# issubset