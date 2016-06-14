def digit_sum(n):
    start=0
    while n//10!=0:
        start=start+(n%10)
        n=n//10
        print start
    else:
        start+=n
    print start
digit_sum(43898)
