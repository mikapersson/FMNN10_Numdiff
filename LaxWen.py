import numpy as np
import scipy.sparse as sp


def LaxWen(u, amu):
    N = len(u)

    # CREATE DIAGONALS (chap6 slide27)
    under = (amu/2)*(1+amu)
    main = 1-amu**2
    over = -(amu/2)*(1-amu)

    diags = np.array([under * np.ones(N - 1), main * np.ones(N), over * np.ones(N - 1)])
    offset = [-1, 0, 1]
    resmat = sp.diags(diags, offset).toarray()

    resmat[N-1, 0] = over
    resmat[0, N-1] = under

    return np.matmul(resmat, u)
