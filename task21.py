from project3.LaxWen import LaxWen as LW
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import numpy as np

# SOLVE THE LNEAR ADVECTION EQUATION

# almost the same as in task 1.1 and 1.2
a = 9/5
N = 30
dx = 1/N
xx = np.linspace(0, 1, N+1)
gx = np.exp(-100*(xx[0: -1]-0.5)**2)  # initial value condition

M = 300
tend = 5  # (2 for 5 peaks)
dt = tend/M
tt = np.linspace(0, tend, M+1)

# HUR BERÄKNAR MAN CFL FÖR DENNA METODEN? a*(dt/dx**2)??
amu = a * (dt/dx)

T, X = np.meshgrid(tt, xx)

solmat = np.zeros((N, M+1))
solmat[:, 0] = gx
uold = gx

# Create vector containing RMS norm
rms = np.zeros(M+1)
rms[0] = np.sqrt(np.mean(np.square(gx)))

for i in range(M):
    unew = LW(uold, amu)
    solmat[:, i+1] = unew
    rms[i+1] = np.sqrt(np.mean(np.square(unew)))
    uold = unew

solmat = np.insert(solmat, len(solmat), solmat[1, :], 0)  # insert the x=1 boundary  WHY DO WE DO THIS?

fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, solmat, cmap='jet')
ax.set_title('task21')
plt.show()

plt.figure(2)
plt.plot(tt, rms)
plt.title("RMS norm of solution over time with a*(dt/dx)=" + str(a*dt/dx))
plt.ylabel("error")
plt.xlabel("time")
plt.show()




