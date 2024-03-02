import numpy as np

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4, 1:4] = z
print(output)

#be careful when copying arrays!!!
a =  np.array([1,2,3])
b = a 
b[0]= 100
#The issue with this is that when you print a it is going to be modified like it was in b
#but if we do b = a.copy(), even when we modify b it is not going to reflect in a, if we print a
print(b)