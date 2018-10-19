import pandas as pd

df = pd.read_csv('iris.csv')
df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
df.head()

from sklearn.model_selection import train_test_split
from sklearn import decomposition

pca = decomposition.PCA()
fa = decomposition.FactorAnalysis()
X = df.values[:, 0:4]
Y = df.values[:, 4]
train, test = train_test_split(X, test_size=0.3)

train_reduced = pca.fit_transform(train)
print(train_reduced)

test_reduced = pca.transform(test)
print(test_reduced)

print(pca.n_components_)
