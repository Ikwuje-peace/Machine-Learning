import random
class Coin():
    def __init__(self, value=1):
        self.faceUp = 'Heads'
        self.value = value
    def flip(self):
        self.faceUp = random.choice(['Head', 'Tail'])
        return self.faceUp