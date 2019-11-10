import scipy.linalg as la
from project1.chap2.RK34step import RK34step
from project1.chap2.newstep import newstep
from project1.chap2.testf import testf as ft
import matplotlib.pyplot as plt
import math


def adaptiveRK34(f, y0, t0, tf, tol):
    t = [t0]  # initiate vectors (time t and solution y)
    y = [y0]
    err0 = tol
    h0 = (abs(tf - t0) * tol ** (1 / 4)) / (100 * (1 + la.norm(f(t0, y0))))
    [ynew, errold] = RK34step(f, y[0], t[0], h0)
    y.append(ynew)
    t.append(t[-1] + h0)
    hnew = newstep(tol, errold, err0, h0, 4)

    while t[-1] < tf:
        [ynew, err] = RK34step(f, y[-1], t[-1], hnew)
        y.append(ynew)
        t.append(t[-1] + hnew)
        hnew = newstep(tol, err, errold, hnew, 4)
        errold = err

        if t[-1] + hnew > tf:
            hnew = tf - t[-1]
            [ynew, err] = RK34step(f, y[-1], t[-1], hnew)
            y.append(ynew)
            t.append(t[-1] + hnew)



    # PLOT GRAPHS BELOW
    # plt.subplot(121)
    # plt.plot(t, y)
    # yreal =[]
    # for ti in t:
    #     yreal.append(math.exp(ti))
    # plt.plot(t, yreal)
    #
    # # calculate error
    # err=[]
    # for i in range(len(yreal)):
    #     err.append(abs(yreal[i] - y[i]))
    # plt.subplot(122)
    # plt.plot(t, err)
    # plt.yscale("log")
    # plt.show()

    # check if we exceed tf below
    # print(t[-1])
    return [t, y]


adaptiveRK34(ft, 1, 0, 1, 10 ** -6)

