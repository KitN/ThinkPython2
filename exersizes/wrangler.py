# Write a file to read text, split it around whitespace, and strip punctuation.
# Make everything lowercase
import re

def snip_paper(filepath):
    """Takes a text file and turns it into a list of lowercase words with no
    punctuation"""
    import string
    punct = [ord(x) for x in string.punctuation]
    cleanerdict = dict()
    cd = cleanerdict.fromkeys(punct, None)
    with open(filepath) as reader:
        rawstring = reader.read()
        fragments = rawstring.split()
        cleanones = []
        for word in fragments:
            cleanones += [word.translate(cd).lower()]
    return cleanones

def freqlist(words):
    freqs = dict()
    for word in words:
        freqs.setdefault(word, 0)
        freqs[word] += 1
    rankings = [x[::-1] for x in freqs.items()]
    rankings.sort(reverse=True)
    return rankings

grimmies = snip_paper('./gutenberg/grimm.txt')
print(freqlist(grimmies))
