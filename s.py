def match(usefulness, months):
    #your code here
    i = 0
    for i in usefulness:
        i += i

    if i >= (100 - 15 * months) :
      return "Match!"
    else:
      return "No match!"

Test.describe("Basic tests")
Test.assert_equals(match([15,24,12], 4), "No match!")
Test.assert_equals(match([26,23,19], 3), "Match!")
Test.assert_equals(match([11,25,36], 1), "No match!")
Test.assert_equals(match([22,9,24], 5), "Match!")
Test.assert_equals(match([8,11,4], 10), "Match!")
Test.assert_equals(match([17,31,21], 2), "No match!")
Test.assert_equals(match([34,25,36], 1), "Match!")
Test.assert_equals(match([35,35,29], 0), "No match!")
Test.assert_equals(match([35,35,30], 0), "Match!")
Test.assert_equals(match([35,35,31], 0), "Match!")
