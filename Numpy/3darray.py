import numpy as np
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

#Get a specific element (work outside in) from the array number to the row number to the column number
print(a[0, 1, 1])

# you can as well do this to get the elements in the second row of all the arrays
print(a[:,1,:])