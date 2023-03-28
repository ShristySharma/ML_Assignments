import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
# Define the coordinates of the points in the triangles
A = np.array([0, 0])
B = np.array([2, 0])
C = np.array([2, 3])
D = np.array([0, 3])
#Generate lines
l_AB = line_gen(A,B)
l_BC = line_gen(B,C)
l_CD = line_gen(C,D)
l_DA = line_gen(D,A)
l_AC = line_gen(A,C)
# Plot the triangles
plt.plot([A[0], B[0]], [A[1], B[1]], 'b')
plt.plot([A[0], D[0]], [A[1], D[1]], 'b')
plt.plot([C[0], B[0]], [C[1], B[1]], 'b')
plt.plot([C[0], D[0]], [C[1], D[1]], 'b')
plt.plot([A[0], C[0]], [A[1], C[1]], 'b')

# Plot the points
plt.plot(A[0], A[1], 'bo')
plt.plot(B[0], B[1], 'bo')
plt.plot(C[0], C[1], 'bo')
plt.plot(D[0], D[1], 'bo')
plt.plot(A[0], C[1], 'bo')
# Label the points
plt.text(A[0]-0.2, A[1]-0.2, 'A', fontsize=12)
plt.text(B[0]+0.1, B[1]-0.2, 'B', fontsize=12)
plt.text(C[0]+0.1, C[1]+0.1, 'C', fontsize=12)
plt.text(D[0]-0.2, D[1]+0.1, 'D', fontsize=12)
plt.show()
plt.grid()
plt.tight_layout()
plt.savefig('fig_1.png')
#plt.savefig('../figs/Figure1.png')

