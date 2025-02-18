import re
a = input("Enter the word ")
b = re.search('[A-Z]{1}([a-z]+)+', a)

print(b)
