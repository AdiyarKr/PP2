import datetime
import math

a = input('Enter a 1st day (YYYY-MM-DD): ')
b = input('Enter a 2nd day (YYYY-MM-DD): ')

day1 = datetime.datetime.strptime(a, '%Y-%m-%d')
day2 = datetime.datetime.strptime(b, '%Y-%m-%d')


diff = abs(day1 - day2)
diff_as_s = diff.total_seconds()
print(diff_as_s)