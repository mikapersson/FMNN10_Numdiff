import scipy.linalg as la
import matplotlib.pyplot as plt
import numpy as np


def eulerstep(A, uold, h):
    return uold * (1 + h * A)


a = np.eye(3)
print(a)
unew = eulerstep(a, 1.5, 0.5)
print("The new value is: {}".format(unew))

# x = np.arange(1, 10, 1)
# y = np.arange(1, 19, 2)
# print(x)
# print(y)
# plt.plot(x, y)
# plt.show()
# # eulerstep(1,1,1)
