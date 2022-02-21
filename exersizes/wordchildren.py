import pudb; pu.db
corpuspath = '../code/words.txt'

lexicon = set()
lexicon.add('i')
lexicon.add('a')
lexicon.add('')

with open(corpuspath) as reader:
    for line in reader:
        stripped = line.strip()
        lexicon.add(stripped)

def bastardkids(word):
    kids = []
    for i in range(len(word)):
        kid = word[0:i] + word[i+1:]
        kids.append(kid)
    return kids

def truekids(word):
    kids = []
    for i in range(len(word)):
        kid = word[0:i] + word[i+1:]
        if kid in lexicon:
            kids.append(kid)
    return kids

def is_shrinkable(word, v=False):
    """ If a string can be reduced to another word, return True"""
    if word == '':
        return True
    possibles = truekids(word)
    for pos in possibles:
        if is_shrinkable(pos, v):
            if v:
                print(pos, end=" ")
            return True
    return False

for word in lexicon:
    if is_shrinkable(word) and len(word) > 9:
        print(word, len(word))
