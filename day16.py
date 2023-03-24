x=int(input("enter a number"))
match x: 
  case 0: 
      print("0")
  # case 5: 
  #     print("5")
  case 5 if(x%5==0):
      print("5 div by 5")
  case _ if x<0: 
      print("negative")

  case _: 
      print(x)