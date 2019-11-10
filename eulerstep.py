import numpy as np


def eulerstep(A, uold, h):
    if isinstance(A, int):
        return uold * (1 + A * h)  # scalar
    else:
        return uold + h * np.matmul(A, uold)
        # return np.matmul(1 + h * A, uold)  # HA KOLL PÅ MATRISMULTIPLIKATION



