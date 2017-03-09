def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(c, bigger(a,b))

def smaller(a,b):
    if a > b:
        return b
    else:
        return a

def smallerest(a,b,c):
    return smaller(c, smaller(a,b))


def set_range(a,b,c,):
    return biggest(a,b,c) - smallerest(a,b,c)
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
