"""
Task
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().

Consider an Example :
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is *9***.

Notes
The numbers are always positive.
The numbers are in the range (1  ≤  a, b, c  ≤  10).
You can use the same operation more than once.
_It's not necessary to place all the signs and brackets.
Repetition in numbers may occur .
You *cannot swap the operands. For instance, in the given example *you cannot get expression (1 + 3) * 2 = 8.
"""
def expression_matter(a, b, c):
    #return # highest achievable result
    r1 = a * (b + c)
    r2 = a * b * c
    r3 = a + b * c
    r4 = (a + b) * c
    r5 = a + b + c
    #print(r1)
    #print(max([r1, r2, r3, r4]))
    return max(r1, r2, r3, r4, r5)
    #return r1

print(expression_matter(1, 1, 1))

"""
Test.it("Small values")
Test.assert_equals(expression_matter(2, 1, 2), 6)
Test.assert_equals(expression_matter(2, 1, 1), 4)
Test.assert_equals(expression_matter(1, 1, 1), 3)
Test.assert_equals(expression_matter(1, 2, 3), 9)
Test.assert_equals(expression_matter(1, 3, 1), 5)
Test.assert_equals(expression_matter(2, 2, 2), 8)

Test.it("Medium values")
Test.assert_equals(expression_matter(5, 1, 3), 20)
Test.assert_equals(expression_matter(3, 5, 7), 105)
Test.assert_equals(expression_matter(5, 6, 1), 35)
Test.assert_equals(expression_matter(1, 6, 1), 8)
Test.assert_equals(expression_matter(2, 6, 1), 14)
Test.assert_equals(expression_matter(6, 7, 1), 48)

Test.it("Mixed values")
Test.assert_equals(expression_matter(2, 10, 3), 60)
Test.assert_equals(expression_matter(1, 8, 3), 27)
Test.assert_equals(expression_matter(9, 7, 2), 126)
Test.assert_equals(expression_matter(1, 1, 10), 20)
Test.assert_equals(expression_matter(9, 1, 1), 18)
Test.assert_equals(expression_matter(10, 5, 6), 300)
Test.assert_equals(expression_matter(1, 10, 1), 12)
"""
