def daymonth(y1,m1,d1,y2,m2,d2):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    dd1 = daysOfMonths[m1-1] - d1
    print dd1
    if y2 > y1:
        if m2 > m1:
            while m1 < m2 - 1:
                d += daysOfMonths[m1 + 1]
                m1 +=1
            return d + dd1 + d2
        elif m2 == m1:
            return d2 - d1
        else:
            dm1 = 0
            dm2 = 0
            while m2 > 0:
                dm2 = dm2 + daysOfMonths[m2 - 1]
                m2 -= 1
                print m2,dm2
            while m1 < 12:
                dm1 = dm1 + daysOfMonths[m1]
                m1 += 1
                print m1,dm1
        return dm1 + dm2 + dd1 + d2
    else:
        while m1 < m2 - 1:
            d += daysOfMonths[m1]
            print d
            m1 +=1
        return d + dd1 + d2


print daymonth(2011,6,30,2012,6,30)
