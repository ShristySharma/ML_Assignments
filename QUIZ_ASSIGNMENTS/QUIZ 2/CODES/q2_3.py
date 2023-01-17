import numpy as np
L = np.array([3,-4,2])
A = np.array([[-2],[3]])
n = np.array([[L[0]],[L[1]]])
c = -1*np.matmul(n.T,A)
L[2] = c
print(L[0],'x+',L[1],'y+',L[2],'=0')
