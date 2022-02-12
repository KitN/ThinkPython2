# ord('a') is 97
def rotate_word(word):
    lowercased = word.lower()
    encrypted = ""
    for letter in word:
        place = ord(letter) % 96
        newplace = (place + 2) % 26
        encrypted = encrypted + chr(97 + newplace)
    return encrypted

print(rotate_word('banana'))
print(rotate_word('abcdefghijklmnopqrstluvwxyz'))
