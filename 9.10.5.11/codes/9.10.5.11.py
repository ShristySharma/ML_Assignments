import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/home/shri/CoordGeo')

from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

a = 1
A = np.array([[-1*a],[0]])
C = np.array([[a],[0]])
O = (A+C)/2
theta_1 = 0.6*np.pi# np.random.rand()
B = a*np.array([[np.cos(theta_1)],[np.sin(theta_1)]])
theta_2 = -0.45*np.pi #np.random.rand()
D = a*np.array([[np.cos(theta_2)],[np.sin(theta_2)]])
cos1 = (C-A).T @ (D-A)/ (np.linalg.norm(C-A)*np.linalg.norm(D-A))
cos2 = (C-B).T @ (D-B)/ (np.linalg.norm(C-B)*np.linalg.norm(D-B))
print(f"Error = {cos1 - cos2}")
#plots
plt.figure(figsize=(10,10))
c1 = circ_gen(O.T,a)
l_AB = line_gen(A,B)
l_BC = line_gen(B,C)
l_AC = line_gen(A,C)
l_AD = line_gen(A,D)
l_CD = line_gen(C,D)
plt.plot(l_AB[0],l_AB[1])
plt.plot(l_BC[0],l_BC[1])
plt.plot(l_AC[0],l_AC[1])
plt.plot(l_AD[0],l_AD[1])
plt.plot(l_CD[0],l_CD[1])
plt.plot(c1[0],c1[1])

points = np.hstack((A,B,C,D,O))

labels = np.array(['A','B','C','D','O'])

for i in range(5):
      plt.text(points[0][i]*1.05,points[1][i]*1.05,labels[i])
plt.scatter(points[0],points[1])
plt.show()
