import re
a = input("Enter the sentence ")
b = re.sub(' ', ',', a)
print(b)