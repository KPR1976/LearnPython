# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def leapyear(year):
    if year % 4 != 0:
         return False
    elif year % 100 != 0:
         return True
    elif year % 400 != 0:
         return False
    else:
         return True

def daymonth(y1,m1,d1,y2,m2,d2):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    dd1 = daysOfMonths[m1 - 1] - d1
    #dd2 = daysOfMonths[m2] - m2
    if m2 == m1:
        return d2 - d1
    elif y1 > y2:
        if m2 > m1:
            while m1 < m2 - 1:
                d += daysOfMonths[m1 + 1]
                m1 +=1
            return d + dd1 + d2
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
            m1 += 1
        return d + dd1 + d2

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #d = abs(day2 - day1)
    m = daymonth(year1, month1,day1, year2, month2,day2)
    #print m
    ly = 0
    y = (year2 - year1) * 365
    #print y
    while year2 >= year1 and month2 != 2:
        if leapyear(year2) == True:
            ly += 1
            #print ly
        year2 -= 1
    return y + m + ly
    # Your code here.
    ##

#print daysBetweenDates(2012,1,1,2012,2,28)

#print leapyear(1996)
# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
