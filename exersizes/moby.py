
filepath = "../code/words.txt"


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, taboos="xyz"):
    for letter in word:
        if letter in taboos:
            return False
    return True

def abecedarian(word):
    for letter in range(1, len(word)):
        n = word[letter]
        p = word[letter-1]
        follows = ord(n) > ord(p)
        if follows:
            continue
        else:
            return False
    return True

def tripledouble(word):
    if len(word) < 6:
        return False
    startplaces = (len(word) % 6) + 1
    for i in range(startplaces):
        section = word[i:i+6]
        if isnapoleon(section):
            return True
    return False

def isnapoleon(word):
    """Only takes a six character string"""
    one = word[0] == word[1]
    two = word[2] == word[3]
    thr = word[4] == word[5]
    if one and two and thr:
        return True
    else:
        return False


forbidfives = [
    "quxyz",
    "xyzwh",
    "qvxyz"
    ]

if __name__=="__main__":
    print(avoids('manpage'))
    with open(filepath) as wrdfile:
        number_of_words = 0
        avoided = 0
        for line in wrdfile:
            number_of_words += 1
            stripped = line.strip()
            if tripledouble(stripped): 
                print(stripped)
            else:
                pass
        print(avoided/number_of_words)
