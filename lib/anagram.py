# your code goes here!

class Anagram():
    def __init__(self, word):
        self.word=word
    
    def match(self, list=[]):
        lists=[]
        for w in list:
            if sorted(self.word) == sorted(w):
                lists.append(w)
        return lists