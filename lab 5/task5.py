import re
a = input("Enter the word ")
b = re.search('a.*b$', a)

print(b)
