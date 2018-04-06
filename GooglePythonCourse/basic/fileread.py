#!/usr/bin/python -tt
import sys


def readfiles(filename):
    words = []
    count = {}
    f = open(filename, 'rU')
    for line in f:
        string = line.split(' ')
        for word in string:
            if word != '':
                words.append(word.lower())
    for word in words:
        if count.get(word) is None:
            count[word] = 1
        else:
            count[word] = count.get(word) + 1
    return count
    f.close()


def print_words(filename):
    count = readfiles(filename)
    for key in sorted(count.keys()):
        print key, count[key]


def print_top(filename):
    count = readfiles(filename)
    for key in sorted(count.keys(), key=count.get, reverse=True)[:20]:
        print key, count[key]




filename = sys.argv[1]
print_words(filename)
