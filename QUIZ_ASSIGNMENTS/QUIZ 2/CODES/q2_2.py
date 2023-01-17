import numpy as np
L = np.array([3,-4,-16])
A = np.array([[-1],[3]])
B = np.array([[0],[4]])
n = np.array([[L[0]],[L[1]]])
m = np.array([[L[1]],[-1*L[0]]])
normal = lambda t: A + t*n
line = lambda t: B + t*m
Mat = np.hstack((n,m))
res = np.matmul(np.linalg.inv(Mat), B-A)
Foot = normal(res[0])
print(Foot)
