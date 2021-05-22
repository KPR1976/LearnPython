"""
In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]

Test.assert_equals(solve([3,4,4,3,6,3]),[4,6,3])
Test.assert_equals(solve([1,2,1,2,1,2,3]),[1,2,3])
Test.assert_equals(solve([1,2,3,4]),[1,2,3,4])
Test.assert_equals(solve([1,1,4,5,1,2,1]),[4,5,2,1])

"""

def solve(arr):
    resarr = arr[:]
    for i in range(len(arr)):
        if i == 0 and arr[i] in arr[i+1:]:
            resarr.remove(arr[i])
        elif arr[i] in arr[i+1:]:
            resarr.remove(arr[i])
    return resarr


print(solve([3,4,4,3,6,3]))
print(solve([1,2,1,2,1,2,3]))
print(solve([1,2,3,4]))
print(solve([1,1,4,5,1,2,1]))
print(solve([1, 2]))
