import scipy.sparse as sp
import numpy as np
import numpy.linalg as la
import math
import matplotlib.pyplot as plt


def SLsolver(N):
    # Solve the problem u'' = lambda * u on the interval 0 to 1 with homogeneous Dirichlet conditions
    # with a chosen number of grid points N
    # Returns: eigenvalues and eigenfunctions of the problem

    h = 1/(N+1)

    k = np.array([np.ones(N - 1), -2 * np.ones(N), np.ones(N - 1)])
    offset = [-1, 0, 1]
    A = 1 / (h ** 2) * sp.diags(k, offset).toarray()

    eigvals, eigfuncs = la.eig(A)

    return eigvals, eigfuncs


# PLOT ERROR FOR THREE EIGENVALUES
# analytic solution/eigenvalues
eig1 = -math.pi**2
eig2 = -(2*math.pi)**2
eig3 = -(3*math.pi)**2
exacteig = np.array([eig1, eig2, eig3])

# use SLsolver
N = [2**i for i in range(2, 11)]
errors = np.zeros((len(N), 3))

for i in range(len(N)):
    ev, ef = SLsolver(N[i])
    ev = -np.sort(-ev)  # sort eigenvalues
    approxeig = np.array([ev[0], ev[1], ev[2]])
    errors[i] = approxeig - exacteig

plt.figure(1)
labels = ["1st eigenvalue", "2nd eigenvalue", "3rd eigenvalue"]

plt.title("Error (of the approximated eigenvalue)")
plt.xlabel("log number of steps N")
plt.legend(plt.loglog(N, errors), labels)
plt.grid()
plt.ylabel("log error ")
plt.show()

# CALCULATE for N = 499
# N = 499
# ev, ef = SLsolver(N)
# ev = -np.sort(-ev)
# print("Three first (smallest abs-vaule): {}".format(str(ev[0]) + ", " + str(ev[1]) + " and " + str(ev[2])))

# PLOT EIGENMODES (see slide 40)
# N = 100
# x = np.linspace(0, 1, N)
#
# ev, ef = SLsolver(N)
# indexes = ev.argsort()[::-1]  # calculate the indexes for the sorting of eigenvalues
# ef = ef[:, indexes]  # sort eigenfunctions
#
# # complete eigenfunctions and grid
# ef1 = np.insert(ef[:, 0], [0, N], [0, 0])
# ef2 = np.insert(ef[:, 1], [0, N], [0, 0])
# ef3 = np.insert(ef[:, 2], [0, N], [0, 0])
# x = np.insert(x, [0, N], [0, 1])
#
# plt.figure(2)
# # for i in range(3):
# #     plt.plot(x, ef[:, i], label=str(i + 1))
#
# plt.plot(x, ef1, label="1")
# plt.plot(x, ef2, label="2")
# plt.plot(x, ef3, label="3")
#
# plt.xlabel("x position")
# plt.ylabel("distance from centre y=0")
# plt.title("First three eigenmodes")
# plt.legend(title="Mode #")
# plt.grid()
# plt.show()






