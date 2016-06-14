def count(sequence, item):
    total = 0
    for i in range(len(sequence)):
        #print sequence[i]
        if sequence[i] == item:
            #print sequence[i]
            total = total + 1
    return total

print count([4, 'foo', 5, 'foo', 5],5)
