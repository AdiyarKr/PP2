import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, end =" ")
        print(self.y)
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(self.x, end =" ")
        print(self.y)
    def dist(self, o_point):
        dis = math.sqrt((self.x - o_point.x)**2 + (self.y - o_point.y)**2)
        print(dis)

point1 = Point(3, 5)
point2 = Point(1, 1)

point1.show()

point1.move(3, 3)

point1.dist(point2)