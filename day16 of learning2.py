class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display (self):
        print("Name:",self.name)
        print("Regno:",self.regno)

t1=teacher("Amudha","19218")
t2=teacher("Gomathi","19219")

t1.display()
t2.display()
        
