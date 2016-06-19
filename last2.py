
def last2(str):
    l = len(str)
    c = 0
    for i in range(len(str) - 2):
        if str[i:i + 2] == str[l - 2: l]:
            c += 1
    return c




print last2('hixxhi') # 1
print last2('xaxxaxaxx') # 1
print last2('axxxaaxx') # 2
