#Initializing different types of Array
#first
# All 0s matrix
#To do this there is a function called np.zeros()
import numpy as np
a = np.zeros(5)
print('a is ',a)
#for a more complex shape
b = np.zeros([2,3])
print('b is ',b)
# for a three dimensional shape
c = np.zeros([2,3,3])
#the first number 2 is the number of arrays, the second and third number is the number of rows and columns
print('c is ', c)

#for a four dimension
d = np.zeros([2,3,3,2])
print('And d is ',d)