def newstep(tol, err, errold, hold, k):
    return (tol / err) ** (2 / (3 * k)) * (tol / errold) ** (-1 / (3 * k)) * hold
