t = int(input())
for i in range(t):
    ans = ""
    for j in range(8):
        stringg = input()
        for char in stringg:
            if char.islower():
                ans += char
    print(ans)


