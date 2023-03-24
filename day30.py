def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * (factorial(n-1))
print(factorial(5))

def fibbo(n):
  if n<=1:
    return n
  else:
    return(fibbo(n-1) + fibbo(n-2))
n = int(input("enter n"))    
for i in range(n):
  print(fibbo(i))