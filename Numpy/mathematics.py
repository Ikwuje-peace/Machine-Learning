import numpy as np
a = np.array([1,2,3,4])
#adds 2 to every element in the array
a *= 2
# same way you can minus too -=2, or *=2 or =+2
#to take sin of all the numbers
b = np.sin(a)
c = np.cos(a)
print(a)
print(b)
print(c)

#Linear Algebra
d = np.ones((2,3))
print(d)

e = np.full((3,2), 2)
print(e)

#to be able to effectively multiply these two arrays we use np.matmul
f = np.matmul(d,e)
print(f)

#To find the determinant of the matrix
g = np.identity(3)
h = np.linalg.det(g)
print(g)
print(h)