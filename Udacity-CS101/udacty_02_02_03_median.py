def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(c, bigger(a,b))

def median(a,b,c):
    big = biggest(a,b,c)
    if a == big:
        return bigger(b,c)
    if b == big:
        return bigger(a,c)
    else:
        return bigger(a,b)

print median(3,4,5)
