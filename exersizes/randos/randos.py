# Some random number stuff

import random

source = """When I consider how my light is spent ere half my days in this dark
world and wide, and that one talent which is death to hide lodged with me
useless, though my soul more bent to serve therewith my maker, lest he
returning chide, 'doth God exact day labor, light denied?' I fondly ask, though
patience, to silence that murmur, soon replies"""

def histogram(text):
    """ Return a character histogram dictionary for the given text."""
    hist = dict()
    for letter in text:
        hist.setdefault(letter, 0)
        hist[letter] += 1
    return hist

def choose_from_hist(hist):
    """ Return a probalistic key from the hist"""
    grabbag = []
    for key, count in hist.items():
        for drop in range(count):
            grabbag.append(key)
    return random.choice(grabbag)

for x in range(20):
    print(choose_from_hist(histogram(source)))
