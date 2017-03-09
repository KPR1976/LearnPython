index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for entry in index:
        if keyword == entry[0]:
            return entry[1]

    return []


print lookup(index,'')
#>>> ['http://udacity.com','http://npr.org']
