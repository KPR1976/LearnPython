def has23(nums):
    return (nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3)



print has23([2, 5]) # True
print has23([4, 3]) # True
print has23([4, 5]) # False
