"""
Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.

test.assert_equals(nearest_sq(1), 1)
test.assert_equals(nearest_sq(2), 1)
test.assert_equals(nearest_sq(10), 9)
test.assert_equals(nearest_sq(111), 121)
test.assert_equals(nearest_sq(9999), 10000)
"""
def nearest_sq(n):
    return int(round(n ** 0.5)) ** 2

print(nearest_sq(10))
