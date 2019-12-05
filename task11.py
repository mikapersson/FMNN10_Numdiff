from project3.eulerstep import eulerstep as estep
from project3.TRstep import TRstep
from mpl_toolkits import mplot3d
import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt


N = 30  # interior position points
dx = 1/(N+1)  # distance between grid points
M = 186  # time points  (186 to examine cfl)
tend = 0.1
dt = tend/M  # distance between time points
xx = np.linspace(0, 1, N+2)
tt = np.linspace(0, tend, M+1)  # VARFÖR inte +2 här?

T, X = np.meshgrid(tt, xx)

# CREATE TOEPLITZ MATRIX
k = np.array([np.ones(N - 1), -2 * np.ones(N), np.ones(N - 1)])
offset = [-1, 0, 1]
Tdx = 1/dx**2 * sp.diags(k, offset).toarray()

# SOLVE THE PDE
solmat = np.zeros((N, M+1))  # initiate matrix containing the solution of PDE
gx = 10*(0.5 - abs(xx[1:-1] - 0.5))  # u(0,x) = gx (initial value)
solmat[:, 0] = gx
uold = gx

for i in range(M):
    # unew = estep(Tdx, uold, dt)  # task 1.1
    unew = TRstep(Tdx, uold, dt)  # task 1.2  # STÄMMER DENNA PLOTTEN?
    # print(unew)
    # print(unew[0])
    # print(unew.shape)
    solmat[:, i+1] = unew
    uold = unew

solmat = np.insert(solmat, [0, len(solmat)], np.zeros(M+1), 0)  # insert boundary conditions
# print(solmat)

# PLOT
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, solmat, cmap='jet')  # https://medium.com/@yzhong.cs/beyond-data-scientist-3d-plots-in-python-with-examples-2a8bd7aa654b
ax.set_title('task11')
plt.show()

cfl = dt/dx**2
print(cfl)  # 0.5166..


