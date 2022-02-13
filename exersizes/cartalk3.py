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

def is_reverse(x,y):
    """ If two ages are the reverse of eachother, returns True."""
    stringx = str(x).zfill(2)
    stringy = str(y).zfill(2)
    if (stringx[0] == stringy[1] and
        stringx[1] == stringy[0]):
        return True
    else:
        return False
    

agetuples = [
        (5, 19),
        (30, 3),
        (81, 18),
        (99, 50)
        ]
for pair in agetuples:
    print(is_reverse(pair[0], pair[1]))

for gap in range(16, 80):
    mom_age = gap
    kid_age = 0
    count = 0
    while mom_age < 100:
        if is_reverse(mom_age, kid_age):
            count += 1
            print(mom_age, kid_age)
        mom_age += 1
        if is_reverse(mom_age, kid_age):
            count += 1
            print(mom_age, kid_age)
        kid_age += 1
    if count >= 8:
        print(gap)
