def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]




print sum2([1, 2, 3]) # 3
print sum2([1, 1]) # 2
print sum2([1, 1, 1, 1]) # 2
print sum2([1])
