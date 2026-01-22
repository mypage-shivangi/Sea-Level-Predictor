import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(8,5))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2051)
    y1 = res1.slope * x1 + res1.intercept
    plt.plot(x1, y1)

    # Create second line of best fit
    df_recent=df[df['Year']>= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051)
    y2 = res2.slope * x2 + res2.intercept
    plt.plot(x2,y2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
