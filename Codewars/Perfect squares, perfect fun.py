"""
Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length).
If not, simply return "Not a perfect square!".

Examples:

1212 returns:
12
12
Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

123123123 returns:
123
123
123
Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.

test.assert_equals(square_it(1), "1")
test.assert_equals(square_it(222), "Not a perfect square!")
test.assert_equals(square_it(234562342342), "Not a perfect square!")
test.assert_equals(square_it(88989), "Not a perfect square!")
test.assert_equals(square_it(112141568), "112\n141\n568")
"""
def square_it(digits):
    digits = str(digits)
    d = len(digits)
    if d ** 0.5  - int(d ** 0.5) == 0:
        l = int(d ** 0.5)
        result = ''
        for i in range(0, d,l):
            result += digits[i:i + l]
            result += '\n'
    else:
        result = 'Not a perfect square!!'
    return result[:-1]

print(square_it(1))
print(square_it(1234))
print(square_it(111))
print(square_it(112141568))
