from project1.chap2.testf import testf
import scipy.linalg as la
import matplotlib.pyplot as plt
import math


def RK4step(f, uold, told, h):
    y1 = f(told, uold)
    y2 = f(told + h/2, uold + h * y1/2)
    y3 = f(told + h/2, uold + h * y2/2)
    y4 = f(told + h, uold + h * y3)

    return uold + h/6 * (y1 + 2*y2 + 2*y3 + y4)


# TEST
interval = [4**i for i in range(11)]

err = []
exact = math.exp(1)
step = []

for N in interval:
    temp = 1
    ht = 1 / N
    for i in range(N):
        temp = RK4step(testf, temp, 0 + ht * i, ht)

    error = la.norm(temp - exact)
    err.append(error)
    step.append(1 / N)

# step.reverse()
# print("step: {}".format(step))
print(err)
plt.loglog(step, err, label="lambda = " + str(1))
plt.grid()
plt.xlabel("log step size")
plt.ylabel("log global error")
plt.show()






