def same_first_last(nums):
    if len(nums) < 1:
        return False
    else:
        return (nums[0] == nums[-1])

"""
def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
 """

print same_first_last([1, 2, 3]) # False
print same_first_last([1, 2, 3, 1]) # True
print same_first_last([1, 2, 1]) # True
print same_first_last([1])
