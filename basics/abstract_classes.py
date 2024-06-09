from abc import ABC, abstractmethod 

class Person(ABC):
    @abstractmethod
    def __init__(self, name, age, gender, activity):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.activity = activity
    
    @abstractmethod
    def do_activity(self):
        pass
    
    def introduce_yourself(self):
        print(f'Hey, my name is: {self.name} and I have {self.age} years')
        
class Student(Person):
    def __init__(self, name, age, gender, activity):
        super().__init__(name, age, gender, activity)
        
    def do_activity(self):
        print(f"I am studying: {self.activity}")
        
class Worker(Person):
    def __init__(self, name, age, gender, activity):
        super().__init__(name, age, gender, activity)
        
    def do_activity(self):
        print(f"I am working on: {self.activity}")
    

victor = Student("Victor", 22, "Masculine", "Maths")
victor_2 = Worker("Victor", 22, "Masculine", "Creating websites")

victor.do_activity()
victor.introduce_yourself()
victor_2.do_activity()