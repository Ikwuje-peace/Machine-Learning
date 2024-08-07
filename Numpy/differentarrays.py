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

#Second for an all 1s matrix
e = np.ones([4,3,2], dtype='int32')
print('E is,', e)

#third for a matrix that is all ones or twos, and you want to indicate what should be on the matrix
f = np.full((2,2), 99, dtype='float32')
print("F is  ", f)

#Any other number (full_like)
g = np.full_like(e, 4)
# if you didnt use fulllike then youll have to use np.full(e.shape, 4)
print("G the full like is ", g)
# To create an array of random  numbers
h = np.random.rand(4,2,)
#to pass in a shape, you could do np.random.random_sample(a.shape)
print(h)
# Random integer values
i = np.random.randint(7, size=(3,3))
print(i)
#for identity matrix
j = np.identity(5)
print(j)
#For repeat array
arr =  np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)