import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt

# a = np.linspace(0, 1, 4)
# print(a)
# print(a[1:-1])

# solmat = np.zeros((4, 6))
# b = [1,2,3,4]
# solmat[:,0] = b
# print(solmat)

# a = np.ones(3)
# o = 2 * np.ones(2)
# k = np.array([a, o])
# A = sp.diags(k, [0, 1]).toarray()
# print(A)

# a = np.exp(np.array([0, 1, 2]))
# print(a)

# RMS  RMS  RMS
# a = [-1, 2, -3, 4, -5]
# print(np.sqrt(np.mean(np.square(a))))

a = np.array([[1, 2], [2, 3], [3, 4]])
b = (2, 3)
c = (3, 4)
print(a.shape)
print("a: {}, b: {}".format(a, b))

