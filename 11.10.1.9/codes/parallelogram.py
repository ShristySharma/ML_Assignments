import numpy as np
from matplotlib import pyplot as plt
import os

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

#Points
A= np.array([[-2],[-1]])
B= np.array([[4],[0]])
C= np.array([[3],[3]])
D= np.array([[-3],[2]])

#Generate lines
l_AB = line_gen(A,B)
l_BC = line_gen(B,C)
l_CD = line_gen(C,D)
l_DA = line_gen(D,A)

#Plot lines and points
plt.plot(A[0][0], A[1][0], 'k.')
plt.text(A[0][0], A[1][0], 'A')
plt.plot(B[0][0], B[1][0], 'k.')
plt.text(B[0][0], B[1][0], 'B')
plt.plot(C[0][0], C[1][0], 'k.')
plt.text(C[0][0], C[1][0], 'C')
plt.plot(D[0][0], D[1][0], 'k.')
plt.text(D[0][0], D[1][0], 'D')
plt.plot(l_AB[0], l_AB[1], 'b')
plt.plot(l_BC[0], l_BC[1], 'b')
plt.plot(l_CD[0], l_CD[1], 'b')
plt.plot(l_DA[0], l_DA[1], 'b')
plt.grid()
plt.tight_layout()
plt.savefig('fig_1.png')
#plt.savefig('../figs/Figure1.png')
