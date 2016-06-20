def reverse3(nums):
    nnums = []
    nnums.append(nums[-1])
    nnums.append(nums[1])
    nnums.append(nums[0])
    return nnums

print reverse3([1, 2, 3]) # [3, 2, 1]
print reverse3([5, 11, 9]) # [9, 11, 5]
print reverse3([7, 0, 0]) # [0, 0, 7]
