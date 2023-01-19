import numpy as np

A = np.array([[5.0],[-1.0],[2.0]])
m = 8.0
c = m/np.linalg.norm(A)
v = c*A
print(v)
