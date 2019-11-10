import matplotlib.pyplot as plt
import numpy as np
from project1.chap1.eulerint import eulerint


def errVSh(A, y0, t0, tf):
    err = []
    step = []

    interval = [2**i for i in range(20)]  # different values of N of size N = 2^k

    for N in interval:
        err.append(eulerint(A, y0, t0, tf, N)[1])
        step.append((tf - t0) / N)

    # step.reverse()
    # print("step: {}".format(step))
    plt.loglog(step, err, label= "lambda = " + str(A))
    print("err: {}".format(err))

    plt.legend()  # uncomment if we plot ONCE
    plt.grid()
    plt.show()


# errVSh(np.ones((3, 3)), 1, 0, 1)

# plot for different A = lambda
# for lam in range(-3,4):
#     errVSh(lam, 1, 0, 1)
#
#
# plt.ylabel("log error")
# plt.xlabel("log step size")
# plt.legend()
# plt.grid()
# plt.show()  # we see that the slope is = 1

# TASK 1.5
M1 = np.array([[-1, 100], [0, -30]])  # A
yi = np.array([[1, 1]]).transpose()  # y0
ti = 0  # t0
te = 10  # tf
errVSh(M1, yi, ti, te)


