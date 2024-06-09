import typing

# Create the parent class


class Person:
    def __init__(self, name: str, age: int, citizenship: str):
        self.name = name
        self.age = age
        self.citizenship = citizenship

    def Talk(self):
        print("Hi, I'm talking a little")


# Create a child class


class Employee(Person):
    def __init__(self, name, age, citizenship, work: str, salary: float):
        super().__init__(name, age, citizenship)
        self.work = work
        self.salary = salary

    def Talk(self):
        print("I'm not talking")


class Artist(Person):
    def __init__(self, skill: str):
        self.skill = skill

    def ShowSkill(self):
        return f"my skill is: {self.skill}"


# Multiple inheritance


class ArtistEmployee(Employee, Artist):
    def __init__(
        self,
        name: str,
        age: int,
        citizenship: str,
        skill: str,
        salary: float,
        business: str,
    ):
        Person.__init__(self, name, age, citizenship)
        Artist.__init__(self, skill)
        self.salary = salary
        self.business = business

    # Polimorfism
    # def ShowSkill(self):
    #    print("All of the skills in the world")

    def ShowYourself(self):
        # To access to this modified method we use self
        # return f'{self.ShowSkill()}'

        # To access to the method of the parent class we use super()
        # return f'{super().ShowSkill()}'

        return f"Hello, my name is: {self.name}, {self.ShowSkill()}, and I work in {self.business}"


# Create object

robert = ArtistEmployee("Robert", 43, "Mexican", "Sing", 100000, "Apple")

print(robert.name)
print(robert.ShowYourself())

# How to know if a class is a subclass of another || if an object is an instance of a class

inherence = issubclass(ArtistEmployee, Artist)
instance = isinstance(robert, ArtistEmployee)

# print(inherence)
# print(instance)
