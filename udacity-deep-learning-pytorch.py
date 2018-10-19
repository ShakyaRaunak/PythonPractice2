import timeit
import numpy as np

"""
# With Numpy, what is the best way to compute the inner product of two vectors? *

v1 = np.arange(10)
v2 = np.arange(10)
print(np.sum(v1 * v2))
print(np.dot(v1, v2))
print(np.array([vect1 * vect2 for vect1, vect2 in zip(v1, v2)]).sum())

print(timeit.timeit("import numpy as np;v1 = np.arange(10);v2 = np.arange(10);np.sum(v1 * v2)", number=10000))
print(timeit.timeit("import numpy as np;v1 = np.arange(10);v2 = np.arange(10);np.dot(v1, v2)", number=10000))
print(timeit.timeit(
    "import numpy as np;v1 = np.arange(10);v2 = np.arange(10);np.array([vect1*vect2 for vect1,vect2 in zip(v1,v2)]).sum()",
    number=10000))

"""

"""

# With Numpy, what’s the best way to compute the inner product of a vector of size 10 with each row in a matrix of size (5, 10)? *

vector1 = np.arange(10)
matrix1 = np.arange(50).reshape(5, 10)
# print(vector1)
# print(matrix1)
# print()
# print(np.dot(vector1, matrix1))    # error
print(np.array([np.dot(row, vector1) for row in matrix1]))
# print(np.matmul(vector1, matrix1))    # error
print(np.dot(matrix1, vector1))
print(np.sum(matrix1 * vector1, axis=1))

print(timeit.timeit(
    "import numpy as np;vector1 = np.arange(10);matrix1 = np.arange(50).reshape(5, 10);np.array([np.dot(row, vector1) for row in matrix1])",
    number=10000))

print(timeit.timeit(
    "import numpy as np;vector1 = np.arange(10);matrix1 = np.arange(50).reshape(5, 10);np.dot(matrix1, vector1)",
    number=10000))

print(timeit.timeit(
    "import numpy as np;vector1 = np.arange(10);matrix1 = np.arange(50).reshape(5, 10);np.sum(matrix1 * vector1, axis=1)",
    number=10000))

"""
