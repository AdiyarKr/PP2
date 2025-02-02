s = input().split()
s2 = map(int, s)
s3 = list(s2)

def spy_game(nums):

    for i in range (0, len(nums)):
        if nums[i] == 0:
            for j in range (i, len(nums)):
                if nums[j] == 0:
                    for k in range (j, len(nums)):
                        if nums[k] == 7:
                            print(True)
                            return True
    print(False)
    return False 
spy_game1 = ([1,2,4,0,0,7,5]) #--> True
spy_game2 = ([1,0,2,4,0,5,7]) #--> True
spy_game3 = ([1,7,2,0,4,5,0]) #--> False

#spy_game(spy_game1)
#spy_game(spy_game2)
#spy_game(spy_game3)

spy_game(s3)