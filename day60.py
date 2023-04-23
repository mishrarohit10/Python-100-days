class Myclass:
    def __init__(self,value):
        self.vvalue = value

    def show(self):
        print(f"{self.vvalue}")

    @property
    def ten_value(self):
        return 10*self.vvalue
    
    @ten_value.setter
    def setnew(self,newval):
        self.vvalue = newval/10

obj = Myclass(10)
obj.setnew = 100
print(obj.ten_value)
obj.show()