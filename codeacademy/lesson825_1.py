def digit_sum(n):
    n = str(n)
    #print ns
    #i = 0
    num = []
    for i in range(len(n)):
        #print int(i)
        num.append(n[i])
    #print len(ns)
    #print num
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i])
        i += 1
    print sum

digit_sum(434798)
