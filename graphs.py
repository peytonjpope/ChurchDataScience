# Description: This script is used to visualize the data in the churches.csv file.
"""
Visualizer

@author: peytonpope
"""

import pandas as pd
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.chained_assignment = None

# Load the data
df = pd.read_csv('/Users/peytonpope/projects/ChurchesVA_DAV/churches.csv')

custom_palette = [
    "#457B9D",  # Blue  unspecified
    "#E63946",  # Red  methodist
    "#2A9D8F",  # Teal  baptist
    "#F4A261",  # Orange  episcopal
    "#A8DADC",  # Light Blue  presbyterian
    "#1D3557",  # Dark Blue  lutheran
    "#E9C46A",  # Yellow  church of god
    "#6A0572",  # Purple  church of christ  
    "#8D99AE",  # Gray-Blue  pentacostal
    "#FF6B6B",  # Soft Red  catholic
    "#4ECDC4",   # Cyan  lds
    "#F3722C"   # Soft Orange mennonite
]

# Scatter plot for all
g = sns.relplot(
    data=df, x='longitude', y='latitude', kind='scatter', s=1, hue='denomination',
    height=6, aspect=1.8, palette=custom_palette, legend=False
)
g.set(xlim=(-125, -65), ylim=(25, 50), xlabel=None, ylabel=None, yticks=[], xticks=[])
g.despine(left=True, bottom=True)
plt.savefig('/Users/peytonpope/projects/ChurchesVA_DAV/dotplot.png', dpi=300, transparent=True)


# Scatter plots for each denomination
i = 0
for den in df['denomination'].unique():
    ndf = df[df['denomination'] == den]
    g = sns.relplot(
        data=ndf, x='longitude', y='latitude', kind='scatter', s=3, hue='denomination',
        height=6, aspect=1.8, palette=[custom_palette[i]], legend=False
    )
    g.set(xlim=(-125, -65), ylim=(25, 50), xlabel=None, ylabel=None, yticks=[], xticks=[])
    g.despine(left=True, bottom=True)
    plt.savefig(f'/Users/peytonpope/projects/ChurchesVA_DAV/dotplot{den}.png', dpi=300, transparent=True)
    i += 1

# Contour Plot for all
g = sns.FacetGrid(df, height=6, aspect=1.8)
g.map(sns.kdeplot, 'longitude', 'latitude', alpha=0.4, fill=True, bw_adjust=.6, cmap="coolwarm", levels=50, thresh=0.1)
g.set(yticks=[], xticks=[], xlabel=None, ylabel=None)
g.despine(left=True, bottom=True)
plt.savefig('/Users/peytonpope/projects/ChurchesVA_DAV/contourplot.png', dpi=300, transparent=True)


# Contour Plots for each denomination
for den in df['denomination'].unique():
    cdf = df[df['denomination'] == den]
    g = sns.FacetGrid(cdf, height=6, aspect=1.8)
    g.map(sns.kdeplot, 'longitude', 'latitude', alpha=0.4, fill=True, bw_adjust=.6, cmap="coolwarm", levels=50, thresh=0.1)
    g.set(yticks=[], xticks=[], xlabel=None, ylabel=None)
    g.despine(left=True, bottom=True) 
    plt.savefig(f'/Users/peytonpope/projects/ChurchesVA_DAV/contourplot{den}.png', dpi=300, transparent=True)

