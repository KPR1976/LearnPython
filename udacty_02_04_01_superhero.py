# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

def fix_machine(debris, product):
    #l = len(product)
    #print l
    i = len(product)
    while i > 0:
            s = product[-i]
            r = debris.find(s)
            if r != -1:
                i -= 1
            else:
                return "Give me something that's not useless next time."
    return product




### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

#print fix_machine('UdaciousUdacitee', 'Udacity')
