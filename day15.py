import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestampH = time.strftime('%H')
print(timestamp)
timestampM = time.strftime('%M')
print(timestamp)
timestampS = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if(int(timestampH)>0 and int(timestampH)<=12):
    print("Good Morning")
elif(int(timestampH)>12 and int(timestampH)<=18):
  print("Good aFternoon")
else:
  print("good evening")