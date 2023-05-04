class Math:
    def __init__(self,num) -> None:
        self.num = num

    def add(self,n):
        self.num = self.num + n

    @staticmethod
    def addd(a,b):
        return a + b

a = Math(5)
print(a.num)
a.add(6)
print(a.num)
print(a.addd(5,7))