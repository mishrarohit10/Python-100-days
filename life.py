# print lexicoraphically smallest concatenation of all strings

def smallestConcatenation(strings):
    strings.sort()
    return ''.join(strings)

n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print(smallestConcatenation(strings))


