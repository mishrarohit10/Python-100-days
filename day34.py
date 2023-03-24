ep1 = {323: 34 , 343: 43, 453:43}
ep2 = {7654:63, 5654:465}
print(ep1)
ep1.update(ep2)
print(ep1)
# ep1.clear()
print(ep1)
ep1.pop(323)
print(ep1)
ep1.popitem()
print(ep1)
del ep1