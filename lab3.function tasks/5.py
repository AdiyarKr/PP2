from itertools import permutations
def Per(s):
    per_list = permutations(s)

    for perm in list(per_list):
         print (''.join(perm))

s = 'ABC'
Per(s)