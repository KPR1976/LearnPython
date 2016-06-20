def max_end3(nums):

    m = max(nums[0], nums[-1])
    nnums = []
    nnums.append(m)
    nnums.append(m)
    nnums.append(m)
    return nnums

"""
#def max_end3(nums):
    big = max(nums[0], nums[2])
    nums[0] = big
    nums[1] = big
    nums[2] = big
    return nums
"""

print max_end3([1, 2, 3]) # [3, 3, 3]
print max_end3([11, 5, 9]) # [11, 11, 11]
print max_end3([2, 11, 3]) # [3, 3, 3]
