def without_end(str):
    l = len(str)
    return str[1:l - 1]



print without_end('Hello') # 'ell'
print without_end('java') # 'av'
print without_end('coding') # 'odin'
