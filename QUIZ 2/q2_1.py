import numpy as np
L1 = np.array([1.732,1,-1])
L2 = np.array([1,1.732,-1])
n1 = np.array([[L1[0]],[L1[1]]])
n2 = np.array([[L2[0]],[L2[1]]])
cosine = np.matmul(n1.T,n2)/(np.linalg.norm(n1)*np.linalg.norm(n2))
angle = np.arccos(cosine)
print(angle)

