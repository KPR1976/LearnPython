def checkio(data):
    data = sorted(data)
    #print data
    number = len(data)
    if number % 2 != 0:
        data.insert(0,data[int(round(number / 2))])
        #data.insert(0, float((data[int(length)] + data[int(length) + 1])) / 2.0)
        #print data
    else:
        data.insert(0, ((data[number / 2] + data[number / 2 - 1]) / 2.0))
        #data.insert(0, int(data([int(length) / 2]))
        #print data
    #replace this for solution
    return data[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(range(1000000)) == 499999.5, "Long."
    print("The local tests are done.")
