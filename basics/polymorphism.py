class Animal:
    def sound(self):
        pass


class Cat:
    def sound(self):
        return "miau"


class Dog:
    def sound(self):
        return "guau"


def make_sound(animal):
    print(animal.sound())


cat = Cat()
dog = Dog()

make_sound(cat)
