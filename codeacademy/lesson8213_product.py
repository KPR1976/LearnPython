

def product(sequence):
    result = 1
    for i in range(len(sequence)):
        result = result * sequence[i]
    return result

print product([4, 6, 5,12,100])
