def squares(a, b):
    for i in range (a, b+1):
        yield i*i
c = int(input())
d = int(input())
f = squares(c,d)
for i in f:
    print(i)