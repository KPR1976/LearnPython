def find_last(s, l):
    lp = -1
    while True:
        pos = s.find(l, lp + 1)
        if pos == -1:
            return lp
        lp = pos





print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0
