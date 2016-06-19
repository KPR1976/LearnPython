def string_match(a, b):
    r = 0
    if len(a) > len(b):
        l = len(b)
    else:
        l = len(a)
    for i in range(l - 1):
        if a[i] == b[i] and a[i + 1] == b[i + 1]:
            r +=1
    return r





print string_match('xxcaazz', 'xxbaaz') # 3
print string_match('abc', 'abc') # 2
print string_match('abc', 'axc') # 0
