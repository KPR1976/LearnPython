def string_bits(str):
    nstr = ""
    let = 0
    while let in range(len(str)):
        nstr = nstr + str[let]
        let += 2
    return nstr


print string_bits('Hello') # 'Hlo'
print string_bits('Hi') # 'H'
print string_bits('Heeololeo') # 'Hello'
