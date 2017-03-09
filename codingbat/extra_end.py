def extra_end(str):
    l = len(str) - 2
    return str[l:] * 3

print extra_end('Hello') # 'lololo'
print extra_end('ab') #'ababab'
print extra_end('Hi') # 'HiHiHi'
