import datetime
from datetime import date
a = str(input())
b = datetime.datetime.strptime(a, '%Y-%m-%d')
c = date.today()

if b == c:
    c = open("fafada.txt", "x")
if b != c:
    print("no")