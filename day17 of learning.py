class student():
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("Student name:",self.name)
        print("Student mark:",self.mark)

s1=student("Santhiya","98")
s1.display()
