import random
import matplotlib.pyplot as plt
import numpy as np

# Function to integrate
f = lambda x: np.sin(x)

# Generate x values for plotting and finding maximum
xl= np.linspace(0, np.pi, 100)
m0= max(xl, key=f)            # Max value of sin(x) in the interval
#counter for pts below the curve
inside_pts= 0
in_x, in_y= [],[]
out_x, out_y= [], []
# total number of random samples
n=int(input("Enter number of random points: "))
# Monte Carlo sampling
for i in range(n):
    # Random point inside bounding rectangle
    x= random.uniform(0, np.pi)
    y= random.uniform(0, m0)
    #if point lies below the curve
    if y<f(x):
        in_x.append(x)
        in_y.append(y)
        inside_pts += 1
    else:
        out_x.append(x)
        out_y.append(y)
# Monte Carlo estimate of the integral
integral=m0*np.pi*inside_pts/n
print("Estimated integral =", integral)
