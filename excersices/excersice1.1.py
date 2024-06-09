import typing


class Student:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age 
        self.course = course
    
    def Study(self):
        print(f"The student {self.name} is studying. ")
        

victor = Student("Victor", 22, "Sexto trimestre")

print(victor.age)