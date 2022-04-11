"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks (number value) that appear.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has two of a kind at least once, False
        otherwise

        Note that a hand with three fives will also 'have a pair'
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two of a kind at least TWICE, False
        otherwise

        Note that a hand with three fives will also 'have a pair'
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >= 2:
            return True
        return False

    def has_three_o_kind(self):
        """Returns True if the hand has a three of a kind, False otherwise

        Overlaps with better hands (e.g. four o' a kind)
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """ Aces high or lo"""
        self.rank_hist()
        prevkey = 0
        count = 0
        for key in self.ranks.keys():
            if key == prevkey + 1:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
            prevkey = key

        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        pass

    def has_four_o_kind(self):
        pass

    def has_straight_flush(self):
        pass

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_straight())
        print('')

