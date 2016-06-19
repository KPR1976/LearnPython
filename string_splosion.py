def string_splosion(str):
    result = ''
    for l in range(len(str)):
        result = result + str[0:l + 1]
    return result




print string_splosion('Code') # 'CCoCodCode'
print string_splosion('abc') # 'aababc'
print string_splosion('ab') # 'aab'
