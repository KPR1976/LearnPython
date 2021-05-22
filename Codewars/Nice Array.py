"""
https://www.codewars.com/kata/nice-array
A Nice array is defined to be an array where for every value n in the array, there is also an element n-1 or n+1 in the array.

example:

[2,10,9,3] is Nice array because
2=3-1
10=9+1
3=2+1
9=10-1
Write a function named isNice/IsNice that returns true if its array argument is a Nice array, else false.
You should also return false if input array has no elements.
"""
def is_nice(arr):
    if len(arr) == 0:
        return False
    for i in range(len(arr)):
        el = arr[i]
        for j in range(len(arr)):
            result = False
            if el == arr[j] + 1 or el == arr[j] - 1:
                result = True
                break
            else:
                result = False
        if result == False:
            return False
    return True
print(is_nice([2,10,9,3]))
#print(is_nice([3,4,5,7]))
#print(is_nice([]))
#print(is_nice([0]))
#print(is_nice([0,2,3]))
#print(is_nice([0,1,2,3,4,5,6,7,8,9]))
