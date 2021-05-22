"""

Given a string of 3 digit numbers separated by whitespace(s), your task is to return a list of sums for each of these numbers in the string.
Each of these 3 digit numbers represent a sequence with first, second and third digits representing the start, the end (which is also included) and the step of a sequence.

Conditions:
If first digit < second digit, then step will be added consectively to generate the sequence.
Input: s = "293", Output: [15] First digit = 2, second digit = 9, step = 3 and the sequence will be [2, 5, 8]
Input: s = "-941", Output: [-35] First digit = -9, second digit = 4, step = 1 and the sequence will be [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

If first digit > second digit, then step will be subracted consectively to generate the sequence.
One should be careful to when the first digit > second digit, the step will Input: s = "702",
Output: [16] First digit = 7, second digit = 0, step = 2 and the sequence will be [7, 5, 3, 1]

If the step size > abs(1 digit - 2 digit), then return just first digit Input: s = "127",
Output: [1] First digit = 1, second digit = 2, step = 7 and the sequence will be [1]

If the third digit = 0, then you have to return [0] Input: s = "-990", Output: [0] First digit = -9, second digit = 9, step = 0

Other example: Input: s = "-941 -393 310 001 -990 -991" Output: [-35, 15, 0, 0, 0, 0]

"""
def range_sum(s):
    sum = 0
    #ss = str(s)
    #s1 = int(ss[0])
    s1 = int(s / 100)
    print(s1)
    s2 = abs(int((s - s1 * 100) / 10))
    print(s2)
    s3 = abs(abs(s) - abs(s1 * 100) - abs(s2 * 10))
    print(s3)
    for i in range(s1, s2+1, s3):
        print(i)
        sum += i
    return sum


#print(range_sum(293))
#print(range_sum(-941))
#print(range_sum(127))
print(range_sum(-990))

"""
test.describe("String to sequence to list of sums test cases")
test.it("Condition 1")
test.assert_equals(range_sum("293"), [15])
print("<COMPLETEDIN::>")

test.it("Condition 2")
test.assert_equals(range_sum("702"), [16])
print("<COMPLETEDIN::>")

test.it("Condition 3")
test.assert_equals(range_sum("127"), [1])
print("<COMPLETEDIN::>")

test.it("Condition 4")
test.assert_equals(range_sum("-990"), [0])
print("<COMPLETEDIN::>")

test.it("Random test")
test.assert_equals(range_sum("-941 -393 310 001 -990 -991"), [-35, 15, 0, 0, 0, 0])
print("<COMPLETEDIN::>")
"""
