languages = [
        "french.txt",
        "italian.txt",
        "german.txt",
        "english.txt"
        ]

def most_frequent(text):
    """ Returns the letter frequencies of the given text"""
    letters = tuple(text)
    freqs = {}
    for let in letters:
        freqs.setdefault(let, 0)
        freqs[let] += 1
    rankedpairs = []
    for key, val in freqs.items():
        rankedpairs += [(val, key)]
    rankedpairs = sorted(rankedpairs)
    rankedpairs = list(reversed(rankedpairs))
    for rank in rankedpairs:
        print(rank[1], end="")
    print()

for lang in languages:
    with open(lang) as reader:
        most_frequent(reader.read())
