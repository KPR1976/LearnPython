import re
from abc import ABC, abstractmethod


# create system
class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


# abstract class with abstract method
class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


# counter words
class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


text = "Hi all, I just wanted to write a quick post to introduce myself - I came across Modern Testing after attending the Testing Festival this week and listened to Alan Page talk about leading a Quality Culture (the best talk of the entire festival in my opinion). \
I’ve worked in many roles over the course of my career to date - from Test Analyst, Lead, Manager, Specialist, Consultant to my current role leading Quality Engineering & Release Management. \
What Alan said in his talk just made sense, and I’m kicking myself for not knowing about Modern Testing sooner - it articulates a lot of what we are doing & what I believe is the way forwards far better than I ever could. \
I’m looking forwards to reading a bit more, listening to some podcasts and getting to know some of you a bit better. Richard"

# create instance of System
system = System(text)
# print(system)

# create instance of WordCounter
counter = WordCounter()
# raise AttributeError: 'WordCounter' object has no attribute 'process_text'
# system.get_processed_text(counter)

# create adapter for system
adapter = WordCounterAdapter(counter)
system.get_processed_text(adapter)
