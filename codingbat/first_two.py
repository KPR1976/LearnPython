def first_two(str):
    if len(str) <= 2:
        return str
    else:
        return str[0:2]





print first_two('Hello') # 'He'
print first_two('abcdefg') # 'ab'
print first_two('ab') # 'ab'
