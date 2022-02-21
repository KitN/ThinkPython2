import random as rnd
import pudb; pu.db

def nestedsum(nest):
    acc = 0
    for t in nest:
        for n in t:
            acc += n
    return acc

def cumsum(integers):
    acc = 0
    t = []
    for i in integers:
        acc += i
        t.append(acc)
    return t

def middle(t):
    return t[1:-1]

def chop(t):
    del t[0]
    del t[-1]
    return None

def is_sorted(t):
    prev = t[0]
    for succ in t[1:]:
        if succ < prev:
            return False
        else:
            prev = succ
            continue
    return True

def is_anagram(word, target):
    if len(word) != len(target):
        return False
    for letter in word:
        target = target.replace(letter, '#', 1)
    if target == "#"*len(word):
        return True
    else:
        return False


    return False

def has_duplicates(t):
    uniques = set(t)
    if len(t) == len(uniques):
        return False
    else:
        return True

def homeroom(n):
    """ Returns a list of birthdays for a homeroom of n students"""
    allbdays = []
    for kid in range(n):
        birthday = rnd.randint(1,365)
        allbdays.append(birthday)
    return allbdays

def paradox_test(n, limit):
    """ For a class of n students, test up to 'limit' times"""
    i = 0
    acc = 0
    while i < limit:
        i += 1
        oneclass = homeroom(n)
        if has_duplicates(oneclass):
            acc += 1
        else:
            continue
    print(acc/limit)

def in_bisect(space, target, leftindex = 0, rightindex=-1):
    if rightindex == -1:
        rightindex =  len(space)-1
    elif leftindex == rightindex:
        if space[0] == target:
            return leftindex
        else:
            return None
    else:
        midindex = len(space) // 2 # Rounded down.
        leftside = space[:midindex] # Not including midindex
        rightside = space[midindex:] # including midindex
        if target < space[midindex]:
            return in_bisect(leftside, target, leftindex, midindex-1)
        else:
            return in_bisect(rightside, target, midindex, rightindex)

paradox_test(13, 1000)

t1 = [1,2,3]
t2 = [4,5,6]
t3 = [7,8,9]

t4 = [t1, t2, t3]
t5 = [1,2,3,4,5,6]

word1 = "rape"
word2 = "pear"
print(in_bisect(t5, 6))
