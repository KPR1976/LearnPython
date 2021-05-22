'''
https://py.checkio.org/mission/nearest-value/solve/
'''
def nearest_value(values: set, one: int) -> int:
    # your code here
    delta = abs(list(values)[0] - one)
    result = list(values)[0]
    for n in values:
        if abs(n - one) < delta:
            delta = abs(n - one)
            result = n
        elif abs(n - one) == delta and n < result:
            delta = abs(n - one)
            result = n
    return result


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value({0,-2},-1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!") 