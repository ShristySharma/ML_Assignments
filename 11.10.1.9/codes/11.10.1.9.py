import numpy as np
import matplotlib.pyplot as plt
A= np.array([[-2],[-1]])
B= np.array([[4],[0]])
C= np.array([[3],[3]])
D= np.array([[-3],[2]])
x1,y1 = [-2,4],[-1,0]
x2,y2 = [4, 3],[0, 3]
x3,y3 = [3,-3],[3,2]
x4, y4=[-2,-3],[-1,2]
a=A-B
b=D-C
c=A-D
d=B-C
if (np.array_equal(a,b) and  np.array_equal(c,d)):
    print("Since both sides of quadrilateral are parallel to each other.It is a Parallelogram")
else:
    print("it is not a parallelogram")
#adding text inside the plot
plt.text(-2.3,-1 , 'A', fontsize = 12)
plt.text(4.1,0 , 'B', fontsize = 12)
plt.text(3.2,3 , 'C', fontsize = 12)
plt.text(-3.3,2 , 'D', fontsize = 12)
plt.plot(x1, y1, c='g')
plt.xlabel("X-axis", fontsize = 5)
plt.ylabel("Y-axis",fontsize = 5)    
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, marker = 'o')
plt.grid()
plt.show()
        
