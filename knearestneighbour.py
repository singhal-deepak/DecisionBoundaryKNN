# -*- coding: utf-8 -*-
"""KNearestNeighbour.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2s2lz7JvOOY7Zb4GAhUe3nW5Ni2ZubF
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import pandas as pd

# change as per asked
n_neighbors = 3

data = [(0, 1, 0), (2, 0, 1), (6,3, 1), (4,4, 0)]
# 1 represent positive class
# data = [(2, 1, 1), (1, 3.5, 1), (3.5,3, 1), (4.5,0.5, -1), (5,2.5, -1), (3,5, -1), (1,4.5, -1)]

df = pd.DataFrame(data)
df.head()

X = df.iloc[:, 0:2]
y = df.iloc[:, 2:3]

print(X)
print(y)

# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset

h = 0.002 # step size in the mesh

# Create color maps
cmap_light = ListedColormap(["orange", "cyan"])
cmap_bold = ["darkorange", "c"]

for weights in ["uniform"]:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    # *************************************************************************hardcoded part, please change
    x_min, x_max = 0 - 1, 6 + 1
    y_min, y_max = 0 - 1, 4 + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)