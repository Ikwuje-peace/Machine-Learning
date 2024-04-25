import random

number = random.randint(10, 80)

if (number // 2 )== 0:
    print("{} is an even number".format(number))
else:
    print("{} is not an even number".format(number))
print(number)

for i in range(0, 21):
    print(i**6, i//3, i*5)

name = str(input('What is your name'))