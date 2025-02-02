class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print(self.length * self.width)

a = int(input())
b = int(input())

s = Rectangle(a, b)
s.area()