#Let's create a simple game
import random

number = random.randint(1, 100)
name = input(str("What is your name "))
print("Welcome {} the game starts now".format(name))
guess = input(int())

if guess == number:
    print('You got the number right')
else:
    print("{} is the correct number".format(number))


#Let's create a simple game
