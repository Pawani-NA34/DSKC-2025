import random
import matplotlib.pyplot as plt
nc=1
i=0
while (i<=1000):
    x= random.random()
    y=random.random()
    i+=1
    if (((x**2)+(y**2))<1):
        nc+=1
        plt.scatter(x,y, color="red")
    else:
        plt.scatter(x,y,color= 'blue')
print(4*nc/i)
plt.show()