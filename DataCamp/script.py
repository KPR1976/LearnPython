"""
x = [-7, 4, 9, -4, 8]
#greater_than_zero = x in x:(lambda n: (n > 0), x)
greater_than_zero = filter(lambda n: (n > 0), x)
print(list(greater_than_zero))
"""
def nth_root(n):
    """Returns the actual_root function"""
    def actual_root(x):
        """Returns the nth root of x"""
        root = x ** (1/n)
        return root
    return actual_root
square_root = nth_root(2)
cube_root = nth_root(3)
print(square_root(25), cube_root(8))
