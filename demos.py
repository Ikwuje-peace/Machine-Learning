import pandas as pd
df = pd.read_csv(r'C:\Users\USER\MachineLearning\weather\weatherdata1.csv')
people = {
    "first":["Peace", "Mary", "Sarah", "Elizabeth"],
    "last": ["Doe", "John", "Doe", "James"]
}
dft = pd.DataFrame(people)
dft["last"] == "Doe"
print(dft)
print(df) #prints the dataframe
print(type(df))
print(df.shape) #prints the number of rows and column
print(df.head) #prints the first five and the last five rows
print(df.info()) #prints the datatype of the dataframe
pd.set_option('display.max_row', 4)