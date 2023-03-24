import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
M = Matrix([[1, 1, -2, 1], [1, 2, 2, 1], [0, 1, -1, 1]])
print("Matrix : {} ".format(M))
M_rref = M.rref()
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref)) 
print( f"( {M_rref[0][0,3]} {M_rref[0][1,3]} {M_rref[0][2,3]} ) x  = 1")

A= np.array([1,1,0])
B= np.array([1,2,1])
C= np.array([-2,2,-1])

# Define the plane function
def plane(x, y):
    return (-normal[0] * x - normal[1] * y - np.dot(normal, A)) * 1. / normal[2]

# Generate the meshgrid
xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))

# Evaluate the plane function
z = plane(xx, yy)

# Plot the plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, z)
ax.scatter(A[0], A[1], A[2], color='red')
ax.scatter(B[0], B[1], B[2], color='red')
ax.scatter(C[0], C[1], C[2], color='red')
plt.show()
