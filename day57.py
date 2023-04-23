class Person:
    name = "HI"
    networth = 465

    def info(self):
        print(f"{self.name} is a {self.networth}")

a = Person()
a.name = "rohit"
print(a.name)
a.info()