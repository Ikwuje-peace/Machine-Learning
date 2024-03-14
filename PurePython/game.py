import random

print('This is a guessning game')

number_of_guess = 5
score = 0
number = random.randint(1, 100)
name = input(str('What is your name '))
print('{}, Thank you for agreeing to do this game with us'.format(name))
print('You have five guesses, try to guess the number')
print(number)
first_guess = input(int())

if first_guess == number:
    number_of_guess = 5
    score = 2
    print(score)
