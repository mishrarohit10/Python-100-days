# for i in range(11):
#   if(i==10):
#     break
#   print("5 X", i+1, "=", 5 * (i+1))
# print("exited loop")

for i in range(11):
  if(i==10):
    print("skip iteration")
    continue
  print("5 X", i, "=", 5 * i)
print("exited loop")