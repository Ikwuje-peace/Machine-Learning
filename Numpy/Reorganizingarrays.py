import numpy as np
before = np.array([[1,2,3,4],[5,6,7,8]])

print(before)
after = before.reshape(8,1)
print(after)

#Vertically stacking vectors and matrix
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2, v2]))
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack([h1,h2]))