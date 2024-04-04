import random
class Coin():
    def __init__(self, value=1):
        self.faceUp = 'Heads'
        self.value = value
    def flip(self):
        self.faceUp = random.choice(['Head', 'Tail'])
        return self.faceUp

values = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
score1 = 0 #Head
score2 = 0 #Tail

for round in range(1,11):
    print('Round ' + str(round))
    coin = Coin(random.choice(values))
    coin.flip()
    print(coin.faceUp)
    if coin.faceUp == 'Head':
        score1 += coin.value
    else:
        score2 += coin.value