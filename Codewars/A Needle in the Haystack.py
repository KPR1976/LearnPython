"""
Can you find the needle in the haystack?
Write a function findNeedle() that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle, so:
Python, Ruby & Elixir
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
"""
def find_needle(haystack):
    # your code here
    return 'found the needle at position ' + str(haystack.index('needle'))

#find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
