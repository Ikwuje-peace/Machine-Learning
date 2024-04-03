import random
class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def toString(self):
        return self.value + " of " + self.suit
    def getRank(self):
        ranks = {
            "Ace": 14,
            "King": 13,
            "Queen": 12,
            "Jack": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4":4,
            "3": 3,
            "2" :2,
        }
        return ranks[self.value]

class Deck():
    def __init__(self):
        self.deck = []
        self.reset() #Add 52 cards
    def reset(self):
        self.deck =[]
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
    def isEmpty(self):
        return (len(self.deck)==0)
    def length(self):
        return len(self.deck)