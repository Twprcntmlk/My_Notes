
from collections import Counter;

def wordFormation(words, letters):
    letterCounter=Counter(letters)

    for word in words:
        wordCounter=Counter(word)
        if len(wordCounter) - len(letterCounter) ==0:

words = ["the", "word", "love", "scott", "finder", "dictionary"]
letters = "fanierdow"

print(wordFormation(words, letters))
