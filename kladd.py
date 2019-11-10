import numpy as np

# errVSh TEST
# A = np.ones((2, 2))
# B = 1
#
# tf = 1
# exact = la.expm(tf * A)
# print("exact: {}".format(exact))
#
# y0 = 1
# N = 4
# h = tf / N
# temp = y0
# for i in range(N):
#     temp = eulerstep(A, temp, h)
#
# approx = temp
# err = approx - exact
# print("approx: {}".format(approx))
# print("err: {}".format(err))
# print("norm of error: {}".format(la.norm(err)))


# TEST subtract vectors
# V1 = [1, 2, 3, 4, 5]
# V2 = [2, 3, 4, 5, 6]
# print(V1)
# V3 = [V2[i] - V1[i] for i in range(len(V1))]
# print(V3)

# TEST eigenvalues
# M1 = np.array([[3,1], [0,2]])
# print("matrix: {}".format(M1))
# eigen = la.eig(M1)
# print("eigenvalues: {}".format(eigen))

# TEST MATRIXMULIPLICATION
M1 = np.array([[-1, 10], [0, -3]])  # 2x2
# M2 = np.array([[1, 1]]).transpose()  # 2x1
# M3 = np.matmul(1 + 10 * M1, M2)
# tf = 10
# exact = la.expm(tf * M1)
#
# print("exact: {}".format(exact))
# print(M3)

# ide = np.eye(len(M1))
print(np.ones(2))
# print(ide)


