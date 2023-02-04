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
A= np.array([[0],[-4]])
B= np.array([[2],[-4]])
C= np.array([[2],[0]])
D= np.array([[0],[0]])
E=(A+B)/2
F=(B+C)/2
G=(D+C)/2
H=(A+D)/2
print('E=',E)
print('F=',F)
print('G=',G)
print('H=',H)
#Generate lines
l_AB = line_gen(A,B)
l_BC = line_gen(B,C)
l_CD = line_gen(C,D)
l_DA = line_gen(D,A)
l_EF = line_gen(E,F)
l_EH = line_gen(E,H)
l_HG = line_gen(H,G)
l_GF = line_gen(G,F)

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

plt.plot(E[0][0], E[1][0], 'k.')
plt.text(E[0][0], E[1][0], 'E')
plt.plot(F[0][0], F[1][0], 'k.')
plt.text(F[0][0], F[1][0], 'F')
plt.plot(G[0][0], G[1][0], 'k.')
plt.text(G[0][0], G[1][0], 'G')
plt.plot(H[0][0], H[1][0], 'k.')
plt.text(H[0][0], H[1][0], 'H')
plt.plot(l_EF[0], l_EF[1], 'b')
plt.plot(l_EH[0], l_EH[1], 'b')
plt.plot(l_HG[0], l_HG[1], 'b')
plt.plot(l_GF[0], l_GF[1], 'b')
plt.grid()
plt.tight_layout()
plt.savefig('parallelogram1.png')
#CALCULATING area
def cross_product_2d(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]
DA=D-A
print('DA=',DA)
DC=D-C
print('DC=',DC)
ABCD= cross_product_2d(DA, DC)
print("\n AREA OF ABCD..\n", ABCD)
GH=G-H
GF=G-F
print('GH=',GH)
print('GF=',GF)
EFGH= cross_product_2d(GH,GF)
print("\n AREA OF EFGH..\n",EFGH)
