import typing

#Creating classes

class CellPhone:
    def __init__(self, brand, model, camera):
        self.brand = brand
        self.model = model 
        self.camera = camera 

#Instancing objects

iphone = CellPhone("Apple", "15 pro max", "48MP")
samsung = CellPhone("Samsung", "S24 ULTRA", "48MP")

print(iphone.camera)

