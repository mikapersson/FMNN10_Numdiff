import numpy as np
import matplotlib.pyplot as plt
from project1.chap2.adaptiveRK34 import adaptiveRK34


def vanderpol(t, u):
    return np.array([[u[0][1], 100 * (1 - u[0][0] ** 2) * u[0][1] - u[0][0]]])


# testing
# a = np.array([[1, 3]])
# print(a)
# print(a[0])
# print(a ** 2)  # element-wise!!

# set up test
t0 = 0
tf = 200
tol = 10 ** -6
y0 = np.array([[2, 0]])
sol = adaptiveRK34(vanderpol, y0, t0, tf, tol)

time = sol[0]
ys = sol[1]
y1 = []
y2 = []

for i in range(len(time)):
    y1.append(ys[i][0][0])
    y2.append(ys[i][0][1])

plt.subplot(121)
plt.plot(time, y2)
plt.subplot(122)
plt.plot(y1, y2)
plt.show()


