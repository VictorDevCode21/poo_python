# Special Methods


class Person():
    #__init__
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    #__str__ 
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    #__repr__
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    #overloading operators
    
    # __add__
    def __add__(self, other):
        new_value = self.age + other.age
        return Person(self.name + other.name, new_value)
    
victor = Person("Victor", 22)
somebody = Person("Name of somebody ", 28)

new_person = somebody + victor
print(new_person.age)
