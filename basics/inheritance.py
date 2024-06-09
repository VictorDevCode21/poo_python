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
        print(f"my skill is: {self.skill}")


# Create object

robert = Employee("Robert", 43, "Mexican", "Developer", 100000)

print(robert.name)
robert.Talk()
