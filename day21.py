def average(a,b):
  print("AVG", (a+b)/2)

average(6,7)

def average(a=2,b=10):
  print("AVG", (a+b)/2)

  # average(b=9)
  return (a+b)/2

 



def name(fname,mname='Bruce', lname='Wayne'):
  print("Hello", fname, mname, lname)
name("Master")

def name2(*name):
    print("Hello,", name[0], name[1], name[2])

name2("James", "Buchanan", "Barnes")

def name3(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name3(mname = "Buchanan", lname = "Barnes", fname = "James")
     














          
  