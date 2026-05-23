import random
import matplotlib.pyplot as plt
inside_pts=1              # Counter for points inside the quarter circle
i=0               # Total number of generated points
while (i<=1000):
    # Random x and y coordinates between 0 and 1
    x= random.random()
    y=random.random()
    i+=1
    if (((x**2)+(y**2))<1):  # Check if the point lies inside the quarter circle
        inside_pts+=1
        plt.scatter(x,y, color="red")   # Plot inside points in red
    # Plot outside points in blue
    else:
        plt.scatter(x,y,color= 'blue')
# Estimate pi using Monte Carlo formula
print(4*inside_pts/i)
plt.show()