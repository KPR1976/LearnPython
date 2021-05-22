'''
https://py.checkio.org/mission/split-pairs/solve/
'''
def split_pairs(a):
    result = []
    # if len(a) % 2 == 0:
    #     count = len(a) // 2
    #     for i in range(count):
    #         result.append(a[i * 2: (i+1) *2])
    # else:
    #     count = len(a) // 2
    #     for i in range(count):
    #         result.append(a[i * 2: (i+1) *2])
    #     result.append(a[-1] + '_')         
    count = len(a) // 2
    for i in range(count):
        result.append(a[i * 2: (i+1) *2])
    if len(a) % 2 != 0:
        result.append(a[-1] + '_')
    return result



if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")