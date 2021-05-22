"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332
110011
54322345
For a given number num, write a function to test if it's a numerical palindrome or not and return a boolean (true if it is and false if not).

Return "Not valid" if the input is not an integer or less than 0.

Test.it("'1221' should return 'True'")
Test.assert_equals(palindrome(1221),True)

Test.it("'123322' should return 'False'")
Test.assert_equals(palindrome(123322),False)

Test.it("'ACCDDCCA' should return 'Not valid'")
Test.assert_equals(palindrome("ACCDDCCA"),"Not valid")

Test.it("'\"1221\"' should return 'Not valid'")
Test.assert_equals(palindrome("1221"),"Not valid")

Test.it("'-450' should return 'Not valid'")
Test.assert_equals(palindrome(-450),"Not valid")
"""
"""
def palindrome(num):
    if type(num) != int or num < 0:
        return 'Not valid'
    num = str(num)
    middle = int(len(num) / 2)
    left = num[:middle]
    if len(str(num)) % 2 != 0:
        right = num[-1:middle:-1]
    else:
        right = num[-1:middle - 1:-1]
    print(right)
    if left == right:
        return  True
    else:
        return False
"""
def palindrome(num):
    return str(num) == str(num)[::-1] if type(num) == int and num > 0 else "Not valid"
    
print(palindrome(145600006541))
