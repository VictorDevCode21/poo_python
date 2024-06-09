import typing


class Student:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age
        self.course = course
    
    def Study(self):
        print("Studying")


name = input("Enter ur name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

student_1 = Student(name=name, age=age, course=course)

print(
    f"""
Student Data: \n \n 
name {student_1.name}
age {student_1.age}
course {student_1.course}
    """
)

while True:
    estudiar = input("Enter estudiar: ")
    if estudiar.lower() == 'estudiar':
        student_1.Study()
        break