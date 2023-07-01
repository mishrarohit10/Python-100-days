def func(n, sum):

    if n == 0:
        print("n is 0")
        return sum
    
    if n % 10 == 0:
        return func(n // 10, sum + 1)
    
    print(n)
    return func(n // 10, sum)

print(func(100, 0))