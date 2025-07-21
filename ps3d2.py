import random
import matplotlib.pyplot as plt
import numpy as np
f=lambda x: np.sin(x)                                # one iner fn
xl=np.linspace(2*np.pi,3*np.pi,100)  
print(xl) # from 2pi to 3pi, including both, giving v values
m0=max(xl, key=f)
print("Maximum of function ",m0)# key=... tells max 'how' to compare items
N_c=0                                                #no. of pts lying within curve
inx, iny, ox, oy= [], [], [], []                     # (x,y) pairs of pts. lying within the curve, outside the curve
n=int(input("Enter total no. of darts to be thrown= "))
for i in range (0,100):
    x=random.uniform(2*np.pi,3*np.pi)
    y=random.uniform(0,m0)                           # taking y values from within the rectangle
    if (y<f(x)):
        inx.append(x), iny.append(y)
        N_c+=1
    
    else:
        ox.append(x), oy.append(y)
print("Integral sinx from 2pi-3pi ", m0*np.pi*N_c/100)
                                         # GRAPH
plt.scatter(inx, iny, color="red",s=10,alpha=0.9, label="inside")
plt.scatter(ox, oy, color= "blue",s=10, label="outside")
plt.axis("square")
plt.legend()
plt.show()