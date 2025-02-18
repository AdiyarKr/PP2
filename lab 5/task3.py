import re
a = input("Enter the word ")
b = re.search('^[a-z]+(?:_[a-z]+)+$', a)
print(b)
