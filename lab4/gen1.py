def squa(n):
    a = 1
    while a <= n:
        yield a*a
        a += 1
b = int(input())
s = squa(b)
for i in s:
    print(i)
