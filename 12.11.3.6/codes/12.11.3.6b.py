import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


A= np.array([1,1,0])
B= np.array([1,2,1])
C= np.array([-2,2,-1])


# Calculate the normal vector of the plane
v1 = C - A
v2 = B - A
normal = np.cross(v1, v2)



# Define the coefficients matrix and the constants vector
a1 = np.array([[1, 1,-2], [1, 2,2],[0,1,-1]])
a2 = np.array([1, 1,1])

# Solve the system of linear equations
X = np.linalg.solve(a1, a2)
# Print the solution vector
print(X)
print('the equation of the plane is given by: ' )
print("{}x  = 1".format(X))
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
