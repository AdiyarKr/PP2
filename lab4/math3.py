import math
a = int(input("number pf sides: "))
b = int(input("length of the side: "))
S = a*b*b/(4*math.tan(math.radians(180/a)))
S = round(S, 3)
print("Area of this polygon ", S)