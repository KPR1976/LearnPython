"""
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

Notes
Array/list size is at least 2.

Array/list numbers could be a mixture of positives, negatives also zeroes .

Input >> Output Examples
adjacentElementsProduct([1, 2, 3]); ==> return 6
Explanation:
The maximum product obtained from multiplying 2 * 3 = 6, and they're adjacent numbers in the array.
adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]); ==> return 50
Explanation:
Max product obtained from multiplying 5 * 10 = 50.

adjacentElementsProduct([-23, 4, -5, 99, -27, 329, -2, 7, -921])  ==>  return -14
Explanation:
The maximum product obtained from multiplying -2 * 7 = -14, and they're adjacent numbers in the array.

Test.it("Positive numbers")
Test.assert_equals(adjacent_element_product([5, 8]), 40)
Test.assert_equals(adjacent_element_product([1, 2, 3]), 6)
Test.assert_equals(adjacent_element_product([1, 5, 10, 9]), 90)
Test.assert_equals(adjacent_element_product([4, 12, 3, 1, 5]), 48)
Test.assert_equals(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)

Test.it("Both positive and negative values")
Test.assert_equals(adjacent_element_product([3, 6, -2, -5, 7, 3]), 21)
Test.assert_equals(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]), 50)
Test.assert_equals(adjacent_element_product([5, 6, -4, 2, 3, 2, -23]), 30)
Test.assert_equals(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]), -14)
Test.assert_equals(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)

Test.it("Contains zeroes")
Test.assert_equals(adjacent_element_product([1, 0, 1, 0, 1000]), 0)
Test.assert_equals(adjacent_element_product([1, 2, 3, 0]), 6)

"""

def adjacent_element_product(array):
    return max(array[i] * array[i+1] for i in range(len(array) - 1))

#print(adjacent_element_product([1, 0, 1, 0, 1000, -66, -666]))
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))
