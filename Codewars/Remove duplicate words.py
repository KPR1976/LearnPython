"""
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:
Input: 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output: 'alpha beta gamma delta'

Test.assert_equals(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
Test.assert_equals(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
"""
def remove_duplicate_words(s):
    words = s.split(' ')
    results = ''
    for word in words:
        if word not in results:
            results += word
            results += ' '
    return results[:-1]


print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))
