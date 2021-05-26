'''
https://py.checkio.org/mission/sort-array-by-element-frequency/solve/
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
Input: Iterable
Output: Iterable
Precondition: elements can be ints or strings
'''
def frequency_sort(items):
    # your code here
    d = {}
    for item in items:
        if item not in d.keys():
            d[item] = 1
        else:
            d[item] += 1
    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    result = []
    for k, v in d.items():
        for i in range(v):
            result.append(k)
            i += 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))
    #print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
