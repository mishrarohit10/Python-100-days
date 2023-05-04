class EMp:
    def __init__(self,name) -> None:
        self.name= name
    
    def show(self):
        print(self.name)

emp1 = EMp("harry")
emp1.show()
EMp.show(emp1)