wordspath = "../code/words.txt"

def store_dict(wordlistfile):
    hashable = dict()
    with open(wordlistfile) as reader:
        count = 0
        for line in reader:
            stripped = line.strip()
            hashable[stripped] = len(stripped)
            count += 1
            if count > 30:
                break
    return hashable

def has_dupes(t):
    countdict = {}
    for elem in t:
        countdict.setdefault(elem, 0)
        countdict[elem] += 1
        if countdict[elem] > 1:
            return True
    return False

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)
    return inverse


containsdupes = 'banana'
nodupes = 'lambo'
print(has_dupes([x**2 for x in range(100)]))
