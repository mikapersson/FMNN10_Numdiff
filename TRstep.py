import numpy as np
import numpy.linalg as la


def TRstep(Tdx, uold, dt):
    I = np.eye(len(Tdx))
    temp = np.matmul((I + dt/2*Tdx), uold)
    left = la.inv(I-dt*Tdx/2)
    res = left.dot(temp)
    # res = la.solve(I-dt*Tdx/2, temp)
    return res