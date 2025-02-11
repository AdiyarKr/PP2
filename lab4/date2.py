from datetime import date, timedelta
a = date.today()
b = a - timedelta(days = 1)
c = a + timedelta(days = 1)
print("today is ", a)
print("yesterday is ", b)
print("tomorrow is ", c)