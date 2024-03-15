import random

print('This is a guessing game')

trials = 5
score = 0
number = random.randint(1, 100)
name = input(str('What is your name '))
print('{}, Thank you for agreeing to do this game with us'.format(name))
print('You have five guesses, try to guess the number')
print(number)
guess = int(input())

if number == guess:
    score =+ 5
    print('{0}, is your score {1}, and you guessed correctly'.format(score, name))
else:
    score = 0
    print('You didnt guess correctly')
