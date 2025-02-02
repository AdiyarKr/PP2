class Shape:
    def __init__ (self, length):
        self.length = length
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
            print(self.length * self.length)

x = int(input())
c = Shape(x)
c.area()
c = Square(x)
c.area()