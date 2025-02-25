mytuple = (True, False, True, True)
mytuple1 = (9, 1, 2, 3, 1, 4)

def f(mytuple):
    return all(mytuple)

print(f(mytuple))
print(f(mytuple1))