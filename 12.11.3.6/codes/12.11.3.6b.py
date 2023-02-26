import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


p1= np.array([1,1,0])
p2= np.array([1,2,1])
p3= np.array([-2,2,-1])


# Calculate the normal vector of the plane
v1 = p3 - p1
v2 = p2 - p1
normal = np.cross(v1, v2)



# Define the coefficients matrix and the constants vector
A = np.array([[1, 1,-2], [1, 2,2],[0,1,-1]])
B = np.array([1, 1,1])

# Solve the system of linear equations
X = np.linalg.solve(A, B)
# Print the solution vector
print(X)
print('the equation of the plane is given by: ' )
print("{}x  = 1".format(X))
# Define the plane function
def plane(x, y):
    return (-normal[0] * x - normal[1] * y - np.dot(normal, p1)) * 1. / normal[2]

# Generate the meshgrid
xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))

# Evaluate the plane function
z = plane(xx, yy)

# Plot the plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, z)
ax.scatter(p1[0], p1[1], p1[2], color='red')
ax.scatter(p2[0], p2[1], p2[2], color='red')
ax.scatter(p3[0], p3[1], p3[2], color='red')
plt.show()
