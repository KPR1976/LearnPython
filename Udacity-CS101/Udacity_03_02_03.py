def list_mean(p):
    n = len(p)
    i = 0
    r = 0.0
# check if empty
    if p == []:
        print "Error, your list is empty"
# check if symmetric
    while i < n:
        r += p[i]
        i += 1
    return float(r / n)


print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
#print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0
