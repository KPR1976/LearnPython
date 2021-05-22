"""
The format
A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name){ return true || false }``
Examples
nameInStr('Across the rivers', 'chris') --> true
            ^      ^  ^^   ^
            c      h  ri   s

Contains all of the letters in 'chris', in order.
nameInStr('Next to a lake', 'chris') --> false

Contains none of the letters in 'chris'.
nameInStr('Under a sea', 'chris') --> false
               ^   ^
               r   s

Contains only some of the letters in 'chris'.
nameInStr('A crew that boards the ship', 'chris') --> false
             cr    h              s i
             cr                h  s i
             c     h      r       s i
             ...

Contains all of the letters in 'chris', but not in order.
nameInStr('A live son', 'Allison') --> false
           ^ ^^   ^^^
           A li   son

Contains all of the correct letters in 'Allison', in order,
but not enough of all of them (missing an 'l').
Note: testing will not be case-sensative.

Test.assert_equals(name_in_str("Across the rivers", "chris"), True)
Test.assert_equals(name_in_str("Next to a lake", "chris"), False)
Test.assert_equals(name_in_str("Under a sea", "chris"), False)
Test.assert_equals(name_in_str("A crew that boards the ship", "chris"), False)
Test.assert_equals(name_in_str("A live son", "Allison"), False)
Test.assert_equals(name_in_str("Just enough nice friends","Jennifer"),False)
Test.assert_equals(name_in_str("thomas","Thomas"),True)
Test.assert_equals(name_in_str("pippippi","Pippi"),True)
Test.assert_equals(name_in_str("pipipp","Pippi"),False)
Test.assert_equals(name_in_str("ppipip","Pippi"),False)

"""
def name_in_str(str, name):
    str, name= str.lower(), name.lower()
    #str = str.lower()
    for i in range(len(name)):
        if name[i] in str:
            result = True
            str = str[str.index(name[i]) + 1:]
        else:
            result = False
            break
    return result

print(name_in_str("!!KDZBQ iHShzMhODKv","qO"))
#'!!KDZBQ iHShzMhODKv' and 'qO'
