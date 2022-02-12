
filepath = "../code/words.txt"


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

with open(filepath) as wrdfile:
    number_of_words = 0
    no_e_words = 0
    for line in wrdfile:
        number_of_words += 1
        stripped = line.strip()
        if has_no_e(stripped):
            no_e_words += 1
        else:
            pass

print(no_e_words/number_of_words)
