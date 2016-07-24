def bigger(a,b):
    if a > b:
        return a
    else:
        return b


def biggest(a,b,c):
    if bigger(a,b) > c:
        return bigger(a,b)
    else:
        return c

"""def biggest(a, b, c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
        return b
    else:
        return c """
print biggest(7,5,6)
