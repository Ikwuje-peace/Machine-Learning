import random

class Dice():
    def __init__(self, numberOfSides=6):
        self._numberOfSides = numberOfSides
        self.value =  1

    def throw(self):
        self.value = random.randint(1, self._numberOfSides)
        return self.value
    
dice1 = Dice(6)
dice1.throw()
print("\n First Dice: ")
print(dice1.value)

dice2 =  Dice(6)
dice2.throw()
print('\n Second Dice')
print(dice2.value)

if dice1.value > dice2.value:
    print('First dice wins')
elif dice1.value < dice2.value:
    print('Second dice')
else:
    print('It is a draw')