word = input(str('\nType in any word in this section and I will count the number of vowels in it '))
class Words():
    def __init__(self, words):
        vowel = 0
        for letter in words:
            if letter in 'aeiouAEIOU':
                vowel += 1
            else:
                pass
        print('There are {0} vowels in the word {1}'.format(vowel, words))

x = Words(word)
print(x)