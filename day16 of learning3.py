class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("add:",self.a+self.b)
    def sub(self):
        print("sub:",self.a-self.b)
    def mul(self):
        print("mul:",self.a*self.b)
    def div(self):
        print("div:",self.a/self.b)

obj1=calculator(5,5)
obj1.add()

obj2=calculator(5,5)
obj2.sub()

obj3=calculator(5,5)
obj3.mul()

obj4=calculator(5,5)
obj4.div()
