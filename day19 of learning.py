class student1:
    def __init__(self,name,age,regno):
        self.name=name
        self.age=age
        self.regno=regno

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Regno:",self.regno)

class student2(student1):
    def __init__(self,name,age,regno):
        super().__init__(name,age,regno)

    def display(self):
        super().display()

class student3(student2):
    def __init__(self,name,age,regno):
        super().__init__(name,age,regno)

    def display(self):
        super().display()

obj1=student3("Santhiya","19","44260048")
obj1.display()
    

