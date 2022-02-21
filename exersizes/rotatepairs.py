corpuspath = "../code/words.txt"

def rotate_word(word, shift):
    """ Take a string and rotates the words around, tape-style.
    word: a string to be rotated
    shift: an integer, how much to rotate the string 'abc' +1 is 'cba'
    """
    shifted = ""
    overflow = word[-shift:] # Takes the last n = shift chars
    secondpart = word[0:-shift]#slicey
    shifted = overflow + secondpart
    return shifted

allwords = {}
with open(corpuspath) as reader:
    for line in reader:
        stripped = line.strip()
        allwords[stripped] = len(stripped)

for key in allwords.keys():
    for r in range(1, len(key)):
        spun = rotate_word(key, r)
        if spun in allwords:
            print(key, spun)
