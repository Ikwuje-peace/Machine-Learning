"""This file is to complete some basic mathematical problems with python"""
class Radian():
    def __init__(self, number):
        self.number = int(number)
        self.degree = number * 57.296
        
x = Radian(34)
print(int(x.degree))