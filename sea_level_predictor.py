import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", alpha=0.5)
    
    # First line of best fit (from 1880 to 2050)
    slope1, intercept1, _, _, _ = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051)
    plt.plot(years_extended, slope1 * years_extended + intercept1, 'r', label="Best Fit 1880-2050")
    
    # Second line of best fit (from 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = stats.linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_future = np.arange(2000, 2051)
    plt.plot(years_future, slope2 * years_future + intercept2, 'g', label="Best Fit 2000-2050")
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    return plt.gca()

# Example usage:
# ax = draw_plot()
# plt.show()
