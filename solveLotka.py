from project1.chap2.lotka import lotka
from project1.chap2.adaptiveRK34 import adaptiveRK34
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

# we solve the Lotka-Volterra equation

# y0 = [1, 1]
y0 = np.array([[1, 1]])
sol = adaptiveRK34(lotka, y0, 100, 120, 10 ** -6)

# check properties of solution
time = sol[0]
animals = sol[1]
# print("length of sol: {}".format(len(sol)))  # 2
# print("how many time point: {}".format(len(time)))  # 69385
# print("type of elements in y: {}".format(type(animals[0])))  # numpy.ndarray
# print("lenght of elements in y: {}".format(len(animals[0])))  # 1, one row with two elements
# print("shape of elements in y: {}".format(animals[0].shape))  # 1x2 (two animals)
#
# # plot
# rabbits = []
# foxes = []
# for i in range(len(time)):
#     rabbits.append(animals[i][0][0])
#     foxes.append(animals[i][0][1])
#
# plt.subplot(131)
# plt.plot(time, rabbits, label = "rabbits over time")
# plt.legend()
#
# plt.subplot(132)
# plt.plot(time, foxes, label = "foxes over time")
# plt.legend()
#
# plt.subplot(133)
# plt.plot(foxes, rabbits, label = "rabbits over foxes")
# plt.legend()
# plt.show()


# check if H(x,y) stays close to it's initial values
# check = []
# for i in range(len(time)):
#     check.append(la.norm(animals[i][0] / y0 - 1))
#
# plt.subplot(131)
# plt.plot(time, check)
# plt.title("linlin")
# plt.subplot(132)
# plt.loglog(time, check)
# plt.title("loglog")
# plt.subplot(133)
# plt.plot(time, check)
# plt.yscale('log')
# plt.title("linlog")
#
# plt.show()


