

class Animal:
    def Eat(self):
        return f'I am eating'
    
class Mammal(Animal):
    def BreastFeed(self):
        return f'I am breasting feed'
    
class Bird(Animal):
    def Fly(self):
        return f'I am Flying'
    
class Bat(Mammal, Bird):
    def __init__(self):
        Mammal.__init__(self)
        Bird.__init__(self)
    
batman = Bat()

print(f'{batman.BreastFeed()} , {batman.Eat()}, {batman.Fly()}')

