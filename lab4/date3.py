from datetime import datetime, timedelta
a = datetime.now()
b = a.replace(microsecond = 0)
print(b)