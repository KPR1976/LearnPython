def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def purify(sequence):
    new = []
    for i in sequence:
        if is_even(i):
            new.append(i)
    return new

print purify([4, 6, 5, 9, 5, 11, 20])
