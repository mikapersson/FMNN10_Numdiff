import numpy as np


def ieulerstep(A, uold, h):
    if isinstance(A, int):
        return uold / (1 - h * A)
    else:
        return np.linalg.solve(np.eye(len(A)) - h * A, uold)
