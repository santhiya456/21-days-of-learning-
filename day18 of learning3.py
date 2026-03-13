class grandfather:
    def house(self):
        print("Grandfather owns a house")

class father(grandfather):
    def car(self):
        print("Father owns a car")

class son(father):
    def bike(self):
        print("sons owns a bike")

s=son()
s.house()

            
