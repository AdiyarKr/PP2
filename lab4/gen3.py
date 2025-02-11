def div_3_and_4(a):
    for i in range(0, a+1):
        if i%3 == 0 and i%4 == 0:
            yield i
a = int(input())
b = div_3_and_4(a)
for i in b:
    print(i)