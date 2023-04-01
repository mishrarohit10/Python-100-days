try:
  a  = int(input("enter a number "))
  print(a)
except:
  print('some error occured')
finally:
  print('Im always executed')