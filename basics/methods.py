import typing

#Creating classes

class CellPhone:
    def __init__(self, brand: str, model: str, camera: str):
        self.brand = brand
        self.model = model 
        self.camera = camera 
        
    #Defining methods
        
    def TakePicture(self):
        print(f"Picture taken from {self.model}")
        
    def SavePicture(self):
        print(f"Picture saved! from your {self.model}")
        
    def DeletePicture(self):
        print(f"Picture deleted! of your {self.model}") 


iphone = CellPhone("Apple", "15 pro max", "48MP")
samsung = CellPhone("Samsung", "S24 ULTRA", "48MP")
print(iphone.camera)

#Using methods

samsung.DeletePicture()
iphone.DeletePicture()
