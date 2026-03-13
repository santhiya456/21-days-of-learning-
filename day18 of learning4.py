class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def area(self):
        print("Area of circle")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")
        
class square(Shape):
    def area(self):
        print("area of square")
        
r=Rectangle()
r.display()
