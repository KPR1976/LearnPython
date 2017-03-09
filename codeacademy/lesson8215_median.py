def median(sequence):
    sequence = sorted(sequence)
    number = len(sequence)
    if number % 2 != 0:
        return sequence[int(round(number / 2))]
    else:
        return (sequence[number / 2] + sequence[number / 2 - 1]) / 2.0

print median([1,3,3,4,1,5,4])
