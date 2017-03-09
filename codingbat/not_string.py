def not_string(str):

    if str[0:3] != 'not':
        return "not " + str
    else:
        return str

print not_string('candy') # 'not candy'
print not_string('x') # 'not x'
print not_string('not bad') # 'not bad'
print not_string('not')
print not_string('nottt')
