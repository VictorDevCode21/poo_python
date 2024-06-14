

class Avatar():
    def __init__(self, name, power, speed ):
        self.name = name
        self.power = power 
        self.speed = speed 
        
    def __repr__(self):
        return f'{self.name} (Power: {self.power}, Speed: {self.speed})'
    
    def __add__(self, an_avatar):
        new_name = self.name + '-' + an_avatar.name
        new_power = round(((self.power + an_avatar.power)/2)**2)
        new_speed = round(((self.speed + an_avatar.speed)/2)**2)
        return Avatar(new_name, new_power, new_speed)
        
naruto = Avatar("Naruto", 100, 1000)
sasuke = Avatar("Sasuke", 100, 800)

narusasu = naruto + sasuke
print(narusasu)