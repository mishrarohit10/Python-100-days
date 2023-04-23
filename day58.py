class Person:
    def __init__(self , n , o):
        print("im a eprson")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("rohit",453)
b = Person("burce",665)
c = Person(1,4)
a.info()
b.info()
c.info()