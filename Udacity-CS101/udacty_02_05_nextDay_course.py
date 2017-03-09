def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
        return year, month,day + 1
    else:
        if month < 12:
            return year,month + 1, 1
        else:
            return year + 1, 1, 1



print nextDay(2012, 12, 30)
