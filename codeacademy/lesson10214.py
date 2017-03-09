def flip_bit(number, n):
    mask = (number << (n - 1))
    #print bin(mask)
    result = number ^ n
    result = bin(result)
    return result

print flip_bit(0b111,2)
#"0b101"
print flip_bit(0b1010101, 3)
#0b1010001
