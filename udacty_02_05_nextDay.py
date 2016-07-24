def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
        newday = day + 1
        newmonth = month
        newyear = year
    elif month < 12:
            newday = 1
            newmonth = month + 1
            newyear = year
    else:
        newday = 1
        newmonth = 1
        newyear = year + 1

    return newyear, newmonth, newday

print nextDay(2012, 12, 30)
