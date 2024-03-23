import random

print('\n This is a guessing game')
name = input(str('What is your name '))
name = name.capitalize()
print('{}, Thank you for agreeing to do this game with us'.format(name))
number = random.randint(1, 100)
trials = 5
score = 20
print('\n {} is your score and you have {} guesses, try to guess the number'.format(score, trials))
print(number)
guess = int(input())


while number != guess:
        score -= 4
        trials -= 1
        print('\n {0}, is your score {1}, and you didnt guess correctly. Try again'.format(score, name))
        print('\n You have {} more guesses left'.format(trials))
        guess = int(input())

        if trials == 0:
            print("\n This is the end of the game, I am so sorry you didnt guess correctly")
            break

if number == guess:
    score += 5
    print('You have guessed correctly. {} is your score.'.format(score))
        
       