def his(nums):
    for i in nums:
        while i > 0:
            print('*', end = '')
            i -= 1
        print('')
num1 = [1, 2, 3, 3]
his(num1)