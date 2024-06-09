# Decorators properties

class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    #getter property
    @property
    def name(self):
        return self.__name

    #setter property
    @name.setter
    def name(self, new_name: str):
        self.__name = new_name
    
    #deleter property
    @name.deleter
    def name(self):
        del self.__name

victor = Person("Victor", 22)

name = victor.name

name = victor.name = "Enrique"

print(name)

#deleter
#del victor.name

print(victor.name)
