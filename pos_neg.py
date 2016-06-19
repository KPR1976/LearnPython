def pos_neg(a, b, negative):
    if negative == True and a < 0 and b < 0:
        return True
    elif negative == False and ((a < 0 and b > 0) or ( a > 0 and b < 0)):
        return True
    else:
        return False



print pos_neg(1, -1, False) # True
print pos_neg(-1, 1, False) # True
print pos_neg(-4, -5, True) # True
print pos_neg(-1, -2, False)
print pos_neg(1,-2, True)
