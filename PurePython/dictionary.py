import random

dictionary = []

with open("words.txt", 'r') as word:
	words = set(word.read().split())
	for text in words:
		dictionary.append(text)

# print(dictionary)


while True:
	computerword = random.choice(dictionary)
	print(computerword)
	shuffle = sorted(computerword)

	for i in shuffle:
		print(i.upper(), end="")
	print("\n Rearrange the above letters to spell the correct english word \n")
	guess = input("Enter your word >> ").lower()

	if guess == computerword:
		print("Hooray you guessed the word \n")
	else:
		print("Wrong guess again  \n")