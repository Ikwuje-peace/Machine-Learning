#Statistics with Numpy
import numpy as np

stats = np.array([[1,2,3],[5,6,7]])
minimum_number = np.min(stats, axis=0)
maximum_number = np.max(stats)
sum = np.sum(stats)
print(sum)
print(maximum_number)
print(minimum_number)