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
    

#main program
deckOfCards = Deck()
deckOfCards.shuffle()
scorePlayer1 = 0
scorePlayer2 = 0
roundNumber = 1

while not deckOfCards.isEmpty():
    print('\n ----- Round '+ str(roundNumber)+ ' ----')
    roundNumber += 1
    card1 = deckOfCards.deal()
    card2 = deckOfCards.deal()
    print('       Card 1 : '+ card1.toString())
    print('       Card 2 : '+ card2.toString())
    if card1.getRank() > card2.getRank():
        print(' Card 1 wins')
        scorePlayer1 += 1
    elif card1.getRank() < card2.getRank():
        print(' Card 2 wins')
        scorePlayer2 += 1
    else:
        print('     It is a draw')
print('\n ----- Game Over -----')
print('Score Player 1 : ' + str(scorePlayer1))
print('Score Player 2 : ' + str(scorePlayer2))

if scorePlayer2 > scorePlayer2:
    print('  Player 1 wins ')
elif scorePlayer1 < scorePlayer2:
    print('Player 2 wins')
else:
    print('It is  a draw')
