def array_front9(nums):
  t = 0
  if len(nums) == 0:
    return False
  for i in range(len(nums)):
      if nums[i] == 9 and i <= 3:
          return True
  return False


print array_front9([1, 2, 9, 3, 4]) # True
print array_front9([1, 2, 3, 4, 9]) # False
print array_front9([1, 2, 3, 4, 5]) # False
print array_front9([])
