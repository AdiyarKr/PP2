has_31 = ([1, 3, 3]) #→ True
has_32 = ([1, 3, 1, 3]) #→ False
has_34 = ([3, 1, 3]) #→ False
def has_33(nums):
    for x in range(0, len(nums) - 1):
        if nums[x] == nums[x + 1] == 3:
            print(True)
            return True
    print(False)
    return False

has_33(has_31) 
has_33(has_32)
has_33(has_34)