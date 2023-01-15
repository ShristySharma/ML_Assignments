import numpy as np
A =np.array([[-5],[-1]])
B =np.array([[3],[-5]])
C = np.array([[5],[2]])
X = B -A
Y = C -A
Area = np.hstack((X,Y))
Area = 0.5*np.linalg.det(X.T@Y)
print(Area)
