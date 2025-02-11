def to_down(n):
    while n>=0:
        yield n
        n -= 1
a = int(input())
b = to_down(a)
for i in b:
    print(i)