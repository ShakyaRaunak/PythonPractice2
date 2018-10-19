import pandas as pd

df = pd.read_csv("iris.csv")
df.columns = ["X1", "X2", "X3", "X4", "Y"]
df.head()

# implementation
from sklearn.model_selection import train_test_split
from sklearn import tree

decision = tree.DecisionTreeClassifier(criterion="gini")
# various techniques like Gini, Information Gain, Chi-square, entropy

X = df.values[:, 0:4]
Y = df.values[:, 4]

# train_test_split -> Split arrays or matrices into random train and test subsets
trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
# test_size -> the proportion of the dataset to include in the test split

decision.fit(trainX, trainY)
print("Accuracy: \n", decision.score(testX, testY))
