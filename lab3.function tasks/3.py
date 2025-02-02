heads = 35
legs = 94


def solve(numheads, numlegs):
    chicken = (numheads*4 - legs)/2
    rabbit = heads - chicken 
    print(rabbit)
    print(chicken)

solve(heads, legs)