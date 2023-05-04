class Employee:
    def __init__(self) -> None:
        self.__name = "Harry"

a = Employee()
# print(a.__name) #cannot be accesed
print(a._Employee__name)  #can be accessed indriectly