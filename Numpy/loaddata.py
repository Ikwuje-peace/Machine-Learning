import numpy as np
import pandas as pd

#to load data from a file to a numpy array
data = pd.read_csv(r'C:\Users\USER\MachineLearning\Numpy\data.csv', delimiter=',')
data_set = np.genfromtxt(r'C:\Users\USER\MachineLearning\Numpy\data.txt', delimiter=',', dtype='int8')

#This works now
print(data)
print('The data from the numpy is ')
print(data_set)