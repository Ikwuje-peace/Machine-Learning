import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as seabornInstance
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
#matplotlib inline
dataset = pd.read_csv(r'C:\Users\USER\MachineLearning\weather\weather_data.csv')
print(dataset.shape)

print(dataset.describe())

dataset.plot(x='Outdoor Drybulb Temperature [C]', y='Outdoor Relative Humidity [%]', style='o')
plt.title('Outdoor Drybulb Temperature Vs Outdoor Relative Humidity')
plt.xlabel('Outdoor Drybulb Temperature')
plt.ylabel('Outdoor Relative Humidity')
plt.show()

plt.figure(figuize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset('Outdoor Relative Humidity'))
plt.show()

#dataslicing
