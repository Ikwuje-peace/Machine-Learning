import numpy as np
# import sys

a = np.array([1,2,3], dtype='int8')
b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])

#Print matrix
print(a)

#get Dimension
print("Dimenison",a.ndim, a.shape, a.dtype, a.itemsize)
#to get the total size of the array
#print(a.size*a.itemsize) or
print(a.nbytes)

#Get Type/Size
print("type", b.dtype, "Size", b.itemsize, "bytes")
print("Dimension for b", b.ndim, b.shape)

#floats are bigger than integers
#Get a specific element [rows, column] start python indexing at zero
print(b[0, 2])

#to get a specific row, it is simple just use [row :] the : sign is for slicing
print(b[1 :])

#to get a specific column, it is simple too just use [:, column] 
#the comma after the slicing is important because if it is not there, it is just going to print out all of the first row
print(b[:, 1])
 
#Getting a little more fancy [startindex:endindex:stepsize]
c = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

print(c[0, 1:6:2])
#to change something in array
#This block of code changes the sixth elementh on the second row to be equals to 20
c[1,5] = 20
print(c)

#to change the elemnts on a column
c[:, 2] = 5
#and if you want the replacement to be two different numbers, you just have to specify
# c[:, 2] = [1, 2]
print(c)