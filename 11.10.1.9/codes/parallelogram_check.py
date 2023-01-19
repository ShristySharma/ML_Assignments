import numpy as np
import matplotlib.pyplot as plt
A= np.array([[-2],[-1]])
B= np.array([[4],[0]])
C= np.array([[3],[3]])
D= np.array([[-3],[2]])
a=A-B
b=D-C
c=A-D
d=B-C
if (np.array_equal(a,b) and  np.array_equal(c,d)):
    print("Since both sides of quadrilateral are parallel to each other.It is a Parallelogram")
else:
    print("it is not a parallelogram")

        
