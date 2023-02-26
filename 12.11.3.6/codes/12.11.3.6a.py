import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
sys.path.insert(0,'/home/shri/CoordGeo')

from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

p1= np.array([1,1,-1])
p2= np.array([6,4,-5])
p3= np.array([-4,-2,3])

m=p2-p3
print('direction vector(m) =', m)
# Calculate the normal vector of the plane
v1 = p3 - p1
v2 = p2 - p1
normal = np.cross(v1, v2)
print("x = {} + \u03BB{}".format(p1, m))
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
ax.text(p1[0],p1[1],p1[2], 'A')
ax.scatter(p2[0], p2[1], p2[2], color='red')
ax.text(p2[0],p2[1],p2[2], 'B')
ax.scatter(p3[0], p3[1], p3[2], color='red')
ax.text(p3[0],p3[1],p3[2], 'C')
x_p3p2=line_gen(p3,p2)
plt.plot(x_p3p2[0],x_p3p2[1],x_p3p2[2])
plt.show()
