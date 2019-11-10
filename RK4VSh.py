import matplotlib.pyplot as plt
from project1.chap2 import RK4int, testf
import numpy as np


def RK4VSh(A, y0, t0, tf):
    err = []
    step = []

    interval = [2**i for i in range(2, 20)]  # different values of N of size N = 2^k

    for N in interval:
        err.append(RK4int(A, y0, t0, tf, N)[1])
        step.append((tf - t0) / N)

    # step.reverse()
    # print("step: {}".format(step))
    plt.loglog(step, err, label= "lambda = " + str(A))
    print("err: {}".format(err))

    # plt.legend()  # uncomment if we plot ONCE
    # plt.grid()
    # plt.show()


# ierrVSh(2, 1, 0, 1)

# plot for different A = lambda
for lam in range(-2, 3):
    RK4VSh(lam, 1, 0, 1)


plt.ylabel("log error")
plt.xlabel("log step size")
plt.legend()
plt.grid()
plt.show()  # we see that the slope is = 1


