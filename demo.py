import pandas as pd
df = pd.read_csv(r'C:\Users\USER\MachineLearning\weather\weatherdata1.csv')
print(df) #prints the dataframe
print(df.shape) #prints the number of rows and column
print(df.head) #prints the first five and the last five rows
print(df.info()) #prints the datatype of the dataframe
pd.set_option('display.max_row', 4)