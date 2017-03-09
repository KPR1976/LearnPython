def front_back(str):
    if len(str) == 1 or len(str) == 0:
        return str
    else:
        return str[len(str) - 1] + str[1:len(str)-1] + str[0]



print front_back('code') # 'eodc'
print front_back('a') # 'a'
print front_back('ab') # 'ba'
print front_back('')
