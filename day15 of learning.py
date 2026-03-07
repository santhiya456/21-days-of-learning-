class student:
    def __init__(self):
        self.name=""
        self.ram=""
    def display(self):
        print("Name",self.name)
        print("Reg No",self.regno)

s1=student()
s2=student()

s1.name="Punitha"
s1.regno="44260049"

s2.name="Thanusuya"
s2.regno="44260048"

s1.display()
s2.display()
