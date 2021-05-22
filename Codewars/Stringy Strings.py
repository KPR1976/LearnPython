"""
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.

"""
def stringy(size):
    result = ''
    for i in range(size):
        if i % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result

def stringyl(size):
    stringyl = lambda size: ('10' * size) [:size]
    return stringyl

print(stringy(4))
print(stringy(5))
print(stringyl(1))
