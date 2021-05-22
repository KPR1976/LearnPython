"""
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers.

Test.assert_equals(count_sheep(1), "1 sheep...");
Test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
Test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
"""

def count_sheep(n):
    # your code
    template = ' sheep...'
    result = ''
    for i in range(n):
        result += str( i+ 1) + template
    return result


print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))
