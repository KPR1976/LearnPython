def checkio(data):
    test = data
    testl = []#print test
    for i in range(len(test)):
        print i
        print test[i]
        print test[i].isdigit()
        print test[i].islower()
        print test[i].isupper()
        #print len(test)
        if int(len(test)) >= 10:
            if test[i].isdigit() == True:
                testl.insert(index=1,object=1)
                print testl
                #return True
            elif test[i].isupper() == True:
                testl.insert(index=2,object=1)
                print testl
                #return True
            elif test[i].islower() == True:
                testl.insert(3,1)
                print testl
                #return True
            else:
            #    return False
                #testl.append(False)
                print testl
        else:
            print testl
            tesl = []
            #return False
            #testl.append(False)

    #replace this for solution
        #return testl

#Some hintsi
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(u'A1213pokl') == False, "1st example"
    #assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    #assert checkio(u'QWERTYqwerty') == False, "4th example"
    #assert checkio(u'123456123456') == False, "5th example"
    #assert checkio(u'QwErTy911poqqqq') == True, "6th example"
