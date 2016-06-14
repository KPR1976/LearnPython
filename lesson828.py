def anti_vowel(text):
    newtext = ""
    #text = lower(text)#i = 0
    for i in range(len(text)):
        if text[i].lower() != 'a' and text[i].lower() != 'o' and text[i].lower() != 'e' and text[i].lower() != 'i' \
        and text[i].lower() != 'u' :
        #newtext = newtext + text[i]
            newtext = newtext + text[i]
        #newtext = text(range(len(text)))
        #print newtext
    return newtext



print anti_vowel('PythAoUn!')
