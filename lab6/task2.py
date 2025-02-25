a = input("Enter the sentence ")
def Upperc(a):
    b = sum(1 for x in a if x.isupper())
    print(b)
def Lowerc(a):
    c = sum(1 for x in a if x.islower())
    print(c)
Upperc(a)
Lowerc(a)