import re
a = input("Enter the word ")
b = re.search('ab{2,3}', a)
print(b)
