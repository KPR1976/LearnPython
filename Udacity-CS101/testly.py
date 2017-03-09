
def leapyear(year):
    if year % 4 != 0:
         return False
    elif year % 100 != 0:
         return True
    elif year % 400 != 0:
         return False
    else:
         return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ly = 0
    while year2 >= year1:
        if leapyear(year2) == True:
            ly += 1
        year2 = year2 - 1
    return ly
        #print ly
        #print year2
        #return ly
    # Your code here.
    ##

print daysBetweenDates(1900,1,1,1999,12,31)

#print leapyear(1996)
# Test routine
