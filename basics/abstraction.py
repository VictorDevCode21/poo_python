

class Car():
    def __init__(self):
        self._state = "Off"

    def TurnItIn(self):
        self._state = "On"
        return "The car is On"
    
    def drive(self):
        if self._state == "Off":
            self._state = "On"
        return "Driving the car"

my_car = Car()
print(my_car._state)

#This is abstraction, I am just passing the method to the user so he can use it.
#Without worring about how it is programmed.

print(my_car.drive())