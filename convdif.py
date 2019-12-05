from project3.TRstep import TRstep
import scipy.sparse as sp
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d


def convinv(u, a, d, dt):
    # Convetion-diffusion solver on [0, 1] and for time in [0, 1].
    N = len(u)
    dx = 1/N

    # Discretization (create circulation matrix)
    under = d/dx**2 + a/(2*dx)
    over = d/dx**2 - a/(2*dx)
    main = -2*d/dx**2

    diags = np.array([under * np.ones(N - 1), main * np.ones(N), over * np.ones(N - 1)])
    offset = [-1, 0, 1]
    A = sp.diags(diags, offset).toarray()
    A[N-1, 0] = over
    A[0, N-1] = under

    unew = TRstep(A, u, dt)

    return unew

# TEST SOLVER
a = 1
d = 0.1  # diffusivity constant
Pe = abs(a/d)
print("Pe-number: {}".format(Pe))

# create grid
N = 30
dx = 1/N
xx = np.linspace(0, 1, N+1)
M = 300
tend = 1
dt = tend/M
tt = np.linspace(0, 1, M+1)
T, X = np.meshgrid(tt, xx)

# solve convdif equation and put solution in solmat
gx = np.exp(-100*(xx[0:-1]-0.5)**2)  # initial value condition
solmat = np.zeros((N, M+1))
solmat[:, 0] = gx
uold = gx

for i in range(M):
    unew = convinv(uold, a, d, dt)
    solmat[:, i+1] = unew
    uold = unew

solmat = np.insert(solmat, len(solmat), solmat[1, :], 0)

# Examine shapes of T, X, solmat
# print("Shapes: T = {}, X = {} and matsol = ".format(T.shape, X.shape, solmat.shape))

fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, solmat, cmap='jet')
ax.set_title('task31')
ax.set(xlabel="position x")
ax.set(ylabel="time t")
plt.show()
















