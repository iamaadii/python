class Shape:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, r):
        self.radius=r
        super().__init__(r,r)
    
    def area(self):
        return 3.14 * super().area()
    
rectangle = Shape(8,9)
print(rectangle.area())

cir=Circle(5)
print(cir.area())