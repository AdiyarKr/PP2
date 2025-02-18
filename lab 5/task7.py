import re
a = input("Enter the sentence ")
pattern = r'(?:^|_)(\w)'
b = re.sub(pattern, lambda x: x.group(1).upper(), a)
print(b)