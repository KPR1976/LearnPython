def censor(text, word):
    text = text.split(" ")
    for i in range(len(text)):
        if text[i] == word:
            text[i] = '*' * len(word)
    return " ".join(text)

print censor('how are you are my friend are', 'are')
