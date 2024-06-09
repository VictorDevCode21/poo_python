class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def PersonData(self):
        return f'The name is {self.name} and the age is {self.age}'

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course 
        
    def Course(self):
        return f'The course of the person is {self.course}'

#person = Person()
student = Student("Victor", 22, "6to trimestre Ing en Sistemas")

print(student.PersonData())
print(student.Course())