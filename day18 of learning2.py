class add:
    def add(self):
        result= 10+5
        print("add:",result)

class sub:
    def sub(self):
        result=10-5
        print("Sub:",result)

class operations(add,sub):
    def ope(self):
        print("Answer")
    

o=operations()
o.add()
o.sub()
