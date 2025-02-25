from time import sleep 

milisec = float(input())
sleep(milisec/1000)

def f(a):
    return a**(1/2)

a = int(input())
sleep(milisec/1000)
print(f(a))