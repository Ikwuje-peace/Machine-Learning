"""This file is to create a simple function that sorts a list"""
fruits = ['mango', 'apple', 'guava', 'orange', 'banana', 'watermelon']
#This function below sorts the list of fruits in alphabetical order
fruit = sorted(fruits)
print(fruit)

"""Or"""
class Numbers():
    def __init__(self, list):
        self.list = []
        self.desc = sorted(list)

        
x = Numbers([23,41,34,54,26,45,67])
print(x.desc)