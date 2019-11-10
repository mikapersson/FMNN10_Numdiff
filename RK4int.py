import scipy.linalg as la
from project1.chap2.RK4step import RK4step
import numpy as np
import math


def RK4int(A, y0, t0, tf, N):
    if isinstance(A, int):  # if A is a scalar
        exact = y0 * math.exp(tf * A)
    else:  # if A is a square matrix
        exact = np.dot(la.expm(tf * A), y0)

    h = (tf - t0) / N
    temp = y0
    for i in range(N):
        temp = RK4step(A, temp, h)

    approx = temp  # approx: 2x1
    # err = la.norm([approx, exact])
    err = la.norm(approx - exact)
    # print("err norm: {}".format(err))
    # print("err abs: {}".format(abs(exact - approx)))
    # return [approx, abs(exact - approx)]
    return [approx, err]