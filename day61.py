class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id 

    def show(self):
        print(self.name, self.id)

e = Employee("Rohan das", 430)
e.show()

class programmer(Employee):
    def showLanguage(self):
        print("Python")
e1= programmer("eogit", 3459)
e1.showLanguage()
e1.show()