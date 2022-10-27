# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import median
from fitter import Fitter, get_distributions


def plot_hist(data: list, bins: int, title: str) -> None:
    plt.hist(data, color="blue", bins=bins)
    plt.xlabel(f"Magnitude of {title} the peak current")
    plt.ylabel("Frequency of peak currents")
    plt.title(f"Magnitude of {title}peak current distribution")
    plt.grid(True)
    plt.savefig(f"Magnitude_{title}_peak_current.png")
    plt.close()


def bestDistributions(data: list, title: str) -> None:
    choosen_distributions = ["lognorm", "exponnorm", "weibull_max", "gamma", "alpha"]
    fitter = Fitter(
        data,
        distributions=choosen_distributions,
        timeout=10000,
    )
    fitter.fit()
    print(f"The top 5 distributions for the {title} peak currents are given below : \n")
    print(fitter.summary())
    print("\n")


# read in the dataset
df = pd.read_csv("../Lightning_Strokes_JHB_20km.csv")

# transform the peak currents to their magnitudes
df["Peak Current Magnitude"] = abs(df["Peak Current"])

# view the data in the dataset
print("The dataset containts the following \n")
print(df.head())
print("\n")

# description of the data
print("The statistical description of the data is as follows :")
print(df.describe())
print("\n")

# get the mean, median and mode
mean = df["Peak Current Magnitude"].mean()
median = df["Peak Current Magnitude"].median()
mode = df["Peak Current Magnitude"].mode()
sd = df["Peak Current Magnitude"].std()
variance = df["Peak Current Magnitude"].var()
print(
    f"The mean is = {mean}, the median is = {median}, the mode is = {mode} and the variance is {variance}."
)
print("\n")

# view how the peak current is distributed
plot_hist(df["Peak Current Magnitude"], 500, "")

# distribution for positive values
positive_currents = df[df["Peak Current"] > 0]
plot_hist(positive_currents["Peak Current Magnitude"], 100, "Positive")

# distribution for positive values
negative_currents = df[df["Peak Current"] < 0]
plot_hist(abs(negative_currents["Peak Current Magnitude"]), 100, "Negative")

# fitting distributions
magnitude_peak_currents = df["Peak Current Magnitude"]
bestDistributions(magnitude_peak_currents, "Magnitude")

# difference in distributions between the positive and negative

# for the positive distribution
bestDistributions(positive_currents["Peak Current"], "Magnitude")

# for the negative distribution
bestDistributions(abs(negative_currents["Peak Current"]), "Magnitude")
