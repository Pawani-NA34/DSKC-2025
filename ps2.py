import random
import matplotlib.pyplot as plt
nc=1
i=0
inx, iny, inz, ox, oy, oz= [],[],[],[],[],[]
while (i<=5000):
    x= random.random()
    y=random.random()
    i+=1
    if (((x**2)+(y**2)+(z**2))<1):
        nc+=1          # lies within sphere
        inx.append(x), iny.append(y), inz.append(z)
    else:
        ox.append(x), oy.append(y)
print("pi = ",4*nc/i)
plt.scatter(inx, iny, color="red",s=10,alpha=0.9, label="inside")
plt.scatter(ox, oy, color= "blue",s=10, label="outside")
plt.axis("square")
plt.legend()
plt.show()