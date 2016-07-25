def split_string(source,splitlist):
    outp = []
    insplit = True
    for char in source:
        print char
        if char in splitlist:
            insplit = True
        else:
            if insplit:
                outp.append(char)
                insplit = False
                print outp
            else:
                outp[-1] = outp[-1] + char
                print outp
    return outp


out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
