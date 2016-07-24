def symmetric(p):
    n = len(p)
    i = 0
# check if empty
    if p == []:
        return True
# check if row_count = col_count
    if n != len(p[0]):
        return False
# check if symmetric
    while i < n:
        j = 0
        while j < n:
            if p[i][j] != p[j][i]:
                return False
            j += 1
        i += 1
    return True




print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([])
#>>> False

print symmetric([[1,2,3],
                [2,3,1]])
#>>> False

print symmetric([[1,2,3]])
#>>> False
