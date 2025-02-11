from datetime import date, timedelta 

today = date.today()
dateofdiff = today - timedelta(days = 5)

print(today.day - 5)
print(dateofdiff)