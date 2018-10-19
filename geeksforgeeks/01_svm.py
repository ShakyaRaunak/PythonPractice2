# https://www.geeksforgeeks.org/classifying-data-using-support-vector-machinessvms-in-python/

"""
Let you have basic understandings from this article before you proceed further. Here I’ll discuss an example about SVM
classification of cancer UCI datasets using machine learning tools i.e. scikit-learn compatible with Python.
"""
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

# creating datasets X containing n_samples Y containing two classes
X, Y = make_blobs(n_samples=500, centers=2, random_state=0, cluster_std=0.40)

# plotting scatters
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show()

"""
What Support vector machines do, is to not only draw a line between two classes here, but consider a region about the 
line of some given width. Here’s an example of what it can look like:
"""
import numpy as np

# creating line space between -1 to 3.5
xfit = np.linspace(-1, 3.5)

# plotting scatter
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')

# plot a line between the different sets of data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
                     color='#AAAAAA', alpha=0.4)

plt.xlim(-1, 3.5)
plt.show()
