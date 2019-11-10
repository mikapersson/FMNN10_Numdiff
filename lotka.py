import numpy as np


def lotka(t, u):
    a = 3
    b = 9
    c = 15
    d = 15

    return np.array([[a * u[0][0] - b * u[0][0] * u[0][1], c * u[0][0] * u[0][1] - d * u[0][1]]])  # GÅR DET ATT GÖRA DETTA SMIDIGARE?


#  u[0][0] is x and u[0][1] is y

# kladd/test
# uold = np.array([[1, 1]])
# a = 3
# b = 9
# c = 15
# d = 15
# test = lotka(1, uold)
# print(uold)
# print(test)

