def daysInMonth(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2:
        return 28
    else:
        return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


print nextDay(2012,12,31)
