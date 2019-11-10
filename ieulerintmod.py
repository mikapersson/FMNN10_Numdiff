import scipy.linalg as la
from project1.chap1.ieulerstep import ieulerstep
import math
import matplotlib.pyplot as plt


def ieulerintmod(A, y0, t0, tf, N):
    h = (tf - t0) / N  # step size
    exact = []  # vector containing the exact values
    if isinstance(A, int):  # if A is a scalar
        for i in range(N + 1):
            exact.append(math.exp(A * i * h))
    else:  # if A is a square matrix
        for i in range(N + 1):
            exact.append(la.expm(A * h * i))

    approx = []  # vector containing the numeric solution
    temp = y0  # initial value
    approx.append(temp)
    err = [exact[0] - approx[0]]
    for i in range(1, N + 1):  # compute approx
        temp = ieulerstep(A, temp, h)
        approx.append(temp)
        err.append(abs(exact[i] - approx[i]))

    # print("errTemp: {}".format(err))
    # print("approx: {}".format(approx))
    # print("exact: {}".format(exact))
    # err = la.norm(err)
    # print("err: {}".format(err))
    return [approx, err]


# TEST
# ieulerintmod(1, 1, 0, 1, 5)

# plot
t = [1/101 * i for i in range(101)]  # tf = 1, t0 = 0, N = 100
e = ieulerintmod(1, 1, 0, 1, 100)[1]
plt.subplot(121)
plt.plot(t, e)
plt.title('linlin')
plt.grid()

plt.subplot(122)
plt.plot(t, e)
plt.yscale('log')
plt.title("linlog")
plt.grid()
plt.show()



