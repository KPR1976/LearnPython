def front_times(str, n):
    if len(str) <= 3:
        return str * n
    else:
        return str[0:3] * n


print front_times('Chocolate', 2) # 'ChoCho'
print front_times('Chocolate', 3) # 'ChoChoCho'
print front_times('Abc', 3) # 'AbcAbcAbc'
print front_times('df',4)
