def reverse(text):
    newtext = ""
    #i = 0
    for i in range(len(text)):
        #newtext = newtext + text[i]
        newtext = text[i] + newtext
        #newtext = text(range(len(text)))
        #print newtext
    return newtext




print reverse('Python!')
