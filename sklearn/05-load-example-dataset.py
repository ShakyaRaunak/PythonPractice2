from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()
print(iris)

# digits.data gives access to the features that can be used to classify the digits samples:
# print(digits.data)

# the ground truth for the digit dataset ie the number corresponding to each digit image that we are trying to learn
# print(digits.target)

from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.)
# gamma ->  Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’; C -> Penalty parameter C of the error term.


# The clf (for classifier) estimator instance is first fitted to the model; that is, it must learn from the model.
# This is done by passing our training set to the fit method. For the training set, we’ll use all the images from our
# dataset, except for the last image, which we’ll reserve for our predicting. We select the training set with the [:-1]
# Python syntax, which produces a new array that contains all but the last item from digits.data:
clf_fit = clf.fit(digits.data[:-1], digits.target[:-1])
print(clf_fit)
"""
SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""

# Now you can predict new values. In this case, you’ll predict using the last image from digits.data. By predicting,
# you’ll determine the image from the training set that best matches the last image.
clf_predict = clf.predict(digits.data[-1:])
print(clf_predict)
