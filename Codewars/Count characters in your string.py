"""
The main idea is to count all the occuring characters(UTF-8) in string.
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
What if the string is empty ? Then the result should be empty object literal { }

test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
"""
"""def count(string):
    result = {}
    if len(string) == 0:
        return result
    else:
        for c in string:
            if c in result.keys():
                result[c] += 1
            else:
                result[c] = 1
    return result
"""
def count(string):
      return {i: string.count(i) for i in string}

print(count('abacadbe'))
print(count(''))
