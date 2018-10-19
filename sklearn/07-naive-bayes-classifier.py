# GaussianNB implements the Gaussian Naive Bayes algorithm for classification. The likelihood of the features is
# assumed to be Gaussian.
from sklearn import datasets

iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0], (iris.target != y_pred).sum()))
