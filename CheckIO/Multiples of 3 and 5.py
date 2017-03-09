def mult35(number):
    r = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            r += i
    return r

print mult35(10000)
