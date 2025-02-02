import math

def vol(rr):
    v = (4/3) * math.pi * pow(rr, 3)
    return v

r = int(input())
print(vol(r))