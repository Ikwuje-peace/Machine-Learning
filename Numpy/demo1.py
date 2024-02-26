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