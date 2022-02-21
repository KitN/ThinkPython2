import pronounce

phonedict = pronounce.read_dictionary()

def make_triggle(word):
    """ Given a word, return the special pair of words
    e.g. WRACK becomes RACK and WACK, by removing and then subbing the W
    """
    firstletter = word[0]
    firstbuzz = word[1:]
    twobuzz = firstletter + firstbuzz[1:]
    return (word, firstbuzz, twobuzz)

homodict = pronounce.read_dictionary()

for ortho, phono in homodict.items():
    triggle = make_triggle(ortho)
    if triggle[1] in homodict and triggle[2] in homodict:
        pro1 = homodict[triggle[0]]
        pro2 = homodict[triggle[1]]
        pro3 = homodict[triggle[2]]
        if pro1 == pro2 and pro2 == pro3:
            print(triggle)
        
