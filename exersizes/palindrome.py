def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    length = len(word)
    if length == 0:
        return True
    elif length == 1:
        return True
    endsAreSame = first(word) == last(word)
    if endsAreSame and is_palindrome(middle(word)):
        return True
    return False

foo = "2002"
print(foo)
print(is_palindrome(foo))
