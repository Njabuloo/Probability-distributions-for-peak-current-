# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import median

# read in the dataset
df = pd.read_csv('../Lightning_Strokes_JHB_20km.csv')

# transform the peak currents to their magnitudes
df['Peak Current Magnitude'] = abs(df['Peak Current'])

# view the data in the dataset
print('The dataset containts the following \n')
print(df.head())

# description of the data
print("The statistical description of the data is as follows :")
print(df.describe())
print('\n')

# get the mean, median and mode
mean = df['Peak Current Magnitude'].mean()
median = df['Peak Current Magnitude'].median()
mode = df['Peak Current Magnitude'].mode()
sd = df['Peak Current Magnitude'].std()
variance = df['Peak Current Magnitude'].var()
print(f'The mean is = {mean}, the median is = {median}, the mode is = {mode} and the variance is {variance}.')
print('\n')

# view how the peak current is distributed
plt.hist(df['Peak Current Magnitude'], color='blue',bins=500)
plt.xlabel('Magnitude of the peak current')
plt.ylabel('No of peak currents')
plt.title('Magnitude peak current distribution')
plt.grid(True)
plt.savefig('Magnitude_peak_current.png')

# distribution for positive values
positive_currents = df[ df['Peak Current'] > 0 ]
plt.hist(positive_currents['Peak Current'], color='blue',bins=500)
plt.xlabel('Magnitude of the positive peak current')
plt.ylabel('No of peak currents')
plt.title('Magnitude of positive peak current distribution')
plt.grid(True)
plt.savefig('Magnitude_peak_current_positive_currents.png')

# distribution for positive values
negative_currents = df[ df['Peak Current'] < 0 ]
plt.hist(abs(negative_currents['Peak Current']), color='blue',bins=500)
plt.xlabel('Magnitude of the negative peak current')
plt.ylabel('No of peak currents')
plt.title('Magnitude of negative peak current distribution')
plt.grid(True)
plt.savefig('Magnitude_peak_current_negative_currents.png')