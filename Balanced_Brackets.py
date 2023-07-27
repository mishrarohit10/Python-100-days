n = int(input())
dict = {'{' : '}', '(' : ')', '[' : ']'}
for i in range(n):
    s = input()
    stack = []
    for j in s:
        if j in dict:
            stack.append(j)
        else:
            if len(stack) == 0:
                stack.append(j)
                break
            elif dict[stack[-1]] == j:
                stack.pop()
            else:
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")