import re
a = input("Enter the sentence ")
b = re.sub('(?<!^)([A-Z])', '_\1', a).lower()
print(b)