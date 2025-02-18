import re
a = input("Enter the sentence ")
b = re.findall('[A-Z][a-z]*', a)
c = ''.join(b)
print(c)