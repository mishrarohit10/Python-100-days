a = int(input())
ans = []
for i in range(1,a+1):
    ans.append(i)
tot = 0
for i, n in enumerate(ans):
    value = n
    count = 0
    value1 = str(value)
    count = value1.count('1')
    tot += count

print(tot)