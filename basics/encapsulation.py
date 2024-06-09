import typing

# Private and public classes


class MyClass:
    def __init__(self):
        # This is a private atribute in py
        self._private_atribute = "value"

        # This is a very private atribute in py
        self.__private_atribute = "value"

    def __talk(self):
        print("hey, how are u?")


object = MyClass()

# print(object._private_atribute)


#getters and setters

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name

victor = Person("Victor", 22)

name = victor.get_name()
print(name)

victor.set_name("Victor 2")
name = victor.get_name()

print(name)
