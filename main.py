# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
from statistics import median
from fitter import Fitter, get_distributions


def plot_hist(data: list, bins: int, title: str) -> None:
    plt.hist(data, color="blue", bins=bins)
    plt.xlabel(f"{title} peak current (KA)")
    plt.ylabel("Frequency of peak currents")
    plt.title(f"{title} peak current distribution")
    plt.grid(True)
    plt.savefig(f"{title}_peak_current.png")
    plt.close()


def bestDistributions(data: list, title: str, choosen_distributions: list) -> None:
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
df = pd.read_csv("Lightning_Strokes_JHB_20km.csv")

# view the data in the dataset
print("The dataset containts the following \n")
print(df.head())
print("\n")

# description of the data
print("The statistical description of the data is as follows :")
print(df.describe())
print("\n")

# get the mean, median and mode
mean = df["Peak Current"].mean()
median = df["Peak Current"].median()
mode = df["Peak Current"].mode()
sd = df["Peak Current"].std()
variance = df["Peak Current"].var()
print(
    f"The mean is = {mean}, the median is = {median}, the mode is = {mode} and the variance is {variance}."
)
print("\n")

# view how the peak current is distributed
plot_hist(df["Peak Current"], 1000, "")

# distribution for positive values
positive_currents = df[df["Peak Current"] > 0]
plot_hist(positive_currents["Peak Current"], 100, "Positive")

# distribution for positive values
negative_currents = df[df["Peak Current"] < 0]
plot_hist(abs(negative_currents["Peak Current"]), 100, "Negative")

# fitting distributions
peak_currents = df["Peak Current"]
choosen_distributions = ["norm", "cauchy", "logistic"]
bestDistributions(peak_currents, "", choosen_distributions)

# difference in distributions between the positive and negative
choosen_distributions = ["lognorm", "exponnorm", "weibull_max", "gamma", "alpha"]

# for the positive distribution
bestDistributions(positive_currents["Peak Current"], "Magnitude", choosen_distributions)

# for the negative distribution
bestDistributions(
    abs(negative_currents["Peak Current"]), "negative", choosen_distributions
)
plt.close()

# plotting the CDFs
sorted_peak_currents = np.sort(peak_currents)
normal_distribution_cdf = ss.norm.cdf(sorted_peak_currents)
cauchy_distribution_cdf = ss.cauchy.cdf(sorted_peak_currents)
logistic_distribution_cdf = ss.logistic.cdf(sorted_peak_currents)
data_points = len(sorted_peak_currents)
sorted_peak_currents_cdf = np.arange(data_points) / float(data_points)
plt.plot(sorted_peak_currents, sorted_peak_currents_cdf, label="Peak current")
plt.plot(sorted_peak_currents, normal_distribution_cdf, label="normal")
plt.plot(sorted_peak_currents, cauchy_distribution_cdf, label="cauchy")
plt.plot(sorted_peak_currents, logistic_distribution_cdf, label="logistic")
plt.grid(True)
plt.xlabel("Peak current (KA)")
plt.ylabel("Probability")
plt.title("Emphirical vs Theoretical CDFs plot")
plt.legend()
plt.savefig("CDFs.png")
plt.close()
