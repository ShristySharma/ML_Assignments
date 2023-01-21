import numpy as np
from matplotlib import pyplot as plt

#Generate line points
def line_gen(P,B):
  len = 10
  dim = P.shape[0]
  x_PB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = P + lam_1[i]*(B-P)
    x_PB[:,i]= temp1.T
  return x_PB


P = np.array([[0.0],[-4.0]])
B = np.array([[8.0],[0.0]])
O = np.array([[0.0],[0.0]])
C = line_gen(P, B)
Q = (P + B)/2
print('THE DIRECTION VECTOR IS IS GIVEN BY:',Q)
print('THE SLOPE IS:',Q[1]/Q[0])
D = line_gen(Q, O)
plt.text(P[0][0], P[1][0],'P')  
plt.text(B[0][0],B[1][0], 'B')  
plt.text(O[0][0],O[1][0], 'O') 
plt.text(Q[0][0],Q[1][0], 'Q')  
plt.plot(C[0], C[1])
plt.plot(D[0], D[1])
plt.grid()
plt.tight_layout()
plt.savefig('fig_1.png')
                          
