def ev(n):
    for i in range(0, n+1):
        if(i % 2 == 0):
            yield i
a = int(input())
b = ev(a)
for i in b:
    print(i)