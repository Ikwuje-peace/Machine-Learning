import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather = pd.read_csv(r'C:\Users\USER\MachineLearning\Numpy\data.csv')
crash_df = sns.load_dataset('weather')
print(crash_df)