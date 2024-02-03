import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#matplotlib inline
dataset = pd.read_csv(r'C:\Users\USER\MachineLearning\weather\weatherdata1.csv')
print(dataset.shape)

print(dataset.describe())

dataset.plot(x='Minimum temperature', y='Maximum temperature', style='o')
plt.title('Minimum temperature Vs  Maximum temperature')
plt.xlabel('Minimum temperature')
plt.ylabel('Maximum temperature')
plt.show()

plt.figure(figsize=(15, 10))
plt.tight_layout()
seabornInstance.distplot(dataset('Maximum temperature'))
plt.show()

#dataslicing
X = dataset['Minimum temperature'].values.reshape(-1, 1)
Y = dataset['Maximum temperature'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
#training the algorithm

#To retrieve the intercept:
print('Intercept', regressor.intercept_)
print('Coefficient', regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

dfl = df.head(25)
dfl.plot(kind='bar', figsize=(16, 10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

print('<ean Absolute Error', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))