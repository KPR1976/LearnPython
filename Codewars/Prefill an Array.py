"""
Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

You have to validate input:

v can be anything (primitive or otherwise)
if v is ommited, fill the array with undefined
if n is 0, return an empty array
if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.

Code Examples

    prefill(3,1) --> [1,1,1]

    prefill(2,"abc") --> ['abc','abc']

    prefill("1", 1) --> [1]

    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
"""
def prefill(n,v='undefined'):
    try:
        result = list([v] * int(n))
    except Exception:
        return str(n) + ' is invalid'
    return result

def prefill1(n,v = 'undefined'):
    try:
        return int(n) * [v]
    except (ValueError,TypeError):
        raise TypeError('{} is invalid'.format(n))

print(prefill(3,1))
print(prefill(2,"abc"))
print(prefill(3, prefill(2,'2d')))
print(prefill1("1", 1))
print(prefill1("xyz", 1))
print(prefill(0, 1))
print(prefill1(1))
print(prefill1(None, 1))
