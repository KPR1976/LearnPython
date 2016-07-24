def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    res = 0
    t = len(array)
    if t <> 0:
         t1 = array[t-1]
    else:
        t1 = 0
    #print t1
    for i in range(len(array)):
        if i % 2 == 0 or i == 0:
            res += array[i]
    return res * t1
    #return res * range(len(array))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
