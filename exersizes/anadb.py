import anagram_sets as anset
import shelve

def store_anagrams(anadict, savefile):
    """ Stores the anagram dictionary in a pickle 'shelf'"""
    db = shelve.open(savefile)
    for key, grams in anadict.items():
        db[key] = grams

def read_anagrams(target, readfile):
    """ Finds the anagrams for a given word in the db."""
    sig = anset.signature(target)
    db = shelve.open(readfile)
    anagrams = db[sig]
    return anagrams

if __name__ == "__main__":
    shelffile = "ana.shelf"
    print(read_anagrams('vile', shelffile))
