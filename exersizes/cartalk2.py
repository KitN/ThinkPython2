def first(word):
    """Returns the first character of a string."""
    return word[0]

def last(word):
    """Returns the last of a string."""
    return word[-1]

def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

if __name__=="__main__":
    for n in range(100000, 1000000):
        numstring = str(n)
        lastfour = numstring[-4:]
        lastfive = str(n+1)[-5:]
        middlefour = str(n+2)[1:5]
        allsix = str(n+3)
        flag = True
        for stage in (lastfour, lastfive, middlefour, allsix):
            if is_palindrome(stage):
                continue
            else:
                flag = False
                break
        if flag:
            print(n)

