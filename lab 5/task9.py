import re

def replF(match_obj):
    return match_obj.group('X') + " " + match_obj.group('Y')



a = input("Enter the sentence ")
b = re.sub('(?P<X>[a-zA-Z])(?P<Y>[A-Z])', replF, a)
print(b)