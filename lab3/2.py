

def Qw(s):
    for i in s:
        if i != i.lower():
            i = i.lower()
            print(i, end = '')
        else:
            i = i.upper()
            print(i, end = '')
    
    return True
a = str(input())
Qw(a)