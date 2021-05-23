'''
https://py.checkio.org/mission/digits-multiplication/solve/
'''
def checkio(number):
    string = str(number)
    mult = 1
    for l in string:
        if int(l) != 0:
            mult = mult * int(l)
    return mult

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1