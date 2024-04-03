import random

class Dice:
    def __init__(self, numberOfSides=6):
        self._numberOfSides = numberOfSides
        self.value =  1

    def throw(self):
        self.value = random.randint(1, self._numberOfSides)
        return self.value