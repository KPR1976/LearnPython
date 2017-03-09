def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a



print combo_string('Hello', 'hi') # 'hiHellohi'
print combo_string('hi', 'Hello') # 'hiHellohi'
print combo_string('aaa', 'b') # 'baaab'
