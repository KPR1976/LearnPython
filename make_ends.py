def make_ends(nums):
    me = []
    me.append(nums[0])
    me.append(nums[-1])
    return me

print make_ends([1, 2, 3]) # [1, 3]
print make_ends([1, 2, 3, 4]) # [1, 4]
print make_ends([7, 4, 6, 2]) # [7, 2]
print make_ends([1])
