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