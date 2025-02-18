import re
a = input("Enter the word ")
b = re.search('ab*', a)
print(b)
