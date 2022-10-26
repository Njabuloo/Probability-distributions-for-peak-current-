# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import median

# read in the dataset
df = pd.read_csv('Lightning_Strokes_JHB_20km.csv')

# view the data in the dataset
print('The dataset containts the following \n')
print(df.head())

# description of the data
print("The statistical description of the data is as follows :")
print(df.describe())

# get the mean, median and mode
mean = df['Peak Current'].mean()
median = df['Peak Current'].median()
mode = df['Peak Current'].mode()
print(f'The mean is = {mean}, the median is = {median} and the mode is = {mode}.')