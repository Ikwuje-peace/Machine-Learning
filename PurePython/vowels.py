class Words():
    def __init__(self, vowels):
        vowel = 0
        for i in vowels:
            if i in 'aeiouAEIOU':
                vowel += 1
                print(i)
            else:
                pass
            print(vowel)

x = Words('Name')
print(x)