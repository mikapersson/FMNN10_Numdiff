import scipy.linalg as la
from project1.chap1.eulerstep import eulerstep
import numpy as np
import math


def eulerint(A, y0, t0, tf, N):
    if isinstance(A, int):  # if A is a scalar
        exact = y0 * math.exp(tf * A)
    else:  # if A is a square matrix
        exact = np.dot(la.expm(tf * A), y0)
        # exact = np.matmul(la.expm(tf * A), y0)

    h = (tf - t0) / N
    temp = y0
    for i in range(N):
        temp = eulerstep(A, temp, h)

    approx = temp  # approx: 2x1
    # err = la.norm([approx, exact])
    err = la.norm(approx - exact)  # FEL HÄR
    # print("err norm: {}".format(err))
    # print("err abs: {}".format(abs(exact - approx)))
    # return [approx, abs(exact - approx)] # HOW DO WE USE THE NORM INSTEAD??
    return [approx, err]


# TEST
# t = np.ones(2)
# eulerint(t, 1, 0, 1, 1)


# print(np.eye(2))
# M = eulerint(np.eye(2), 1, 0, 1, 1)
# print("Result: {}".format(M[1]))
y0 = np.array([[1, 1]]).transpose()
e = eulerint(np.eye(2), y0, 0, 1, 10)
print(e)
#
# a = 0
# b = 10
# d=90
# h = (b - a) / d
# print("Intervall: {}".format(h))
# print("Endpoint: {}".format(a + h*d))


# TASK 1.5



