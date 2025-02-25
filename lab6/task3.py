a = str(input("Enter the sentence "))
def Pol(a):
    b = ''.join(i for i in reversed(a))
    if b == a:
        print ("YES")
    else:
        print ("NO")
Pol(a)