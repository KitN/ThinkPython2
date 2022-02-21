corpuspath = "../code/words.txt"

def unique_chars(word):
    """ Returns a sorted string containing the unique characters"""
    ordered = sorted(word)
    return "".join(ordered)

with open(corpuspath) as reader:
    lexicon = []
    for line in reader:
        stripped = line.strip()
        lexicon.append(stripped)

def test_metathesis(word, anagram):
    """ Tests if a word and an anagram are a metathesis pair
    This is only true if the words are I. Anagrams II. Differ in two places
    """
    count = 0
    for para in zip(word, anagram):
        if para[0] != para[1]:
            count += 1
    return count == 2

anagrams = dict()

for word in lexicon:
    makeup = unique_chars(word)
    anagrams.setdefault(makeup, [])
    anagrams[makeup].append(word)


highscores = []
for key, value in anagrams.items():
    score = (len(value), value)
    highscores.append(score)
highscores.sort(reverse=True)

print(test_metathesis('conserve', 'converse'))

for hs in highscores:
    for ana in hs[1]:
        for gram in hs[1]:
            caught_one = test_metathesis(ana,gram)
            if caught_one:
                print(ana, gram)
