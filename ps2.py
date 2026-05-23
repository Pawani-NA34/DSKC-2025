import random
import matplotlib.pyplot as plt

# Number of points inside the sphere
inside_pts = 0
# Total number of random points
total_pts = 5000
in_x, in_y = [], []
out_x, out_y = [], []
# Generate random points
for i in range(total_pts):
    # Random coordinates between 0 and 1
    x= random.random()
    y= random.random()
    z= random.random()
    # whether point lies inside the unit sphere
    if (x**2 + y**2 + z**2) < 1:
        inside_pts += 1
        # Store inside points
        in_x.append(x)
        in_y.append(y)
    else:
        # Store outside points
        out_x.append(x)
        out_y.append(y)

# Estimate pi using Monte Carlo method
pi_est= 6 * inside_pts / total_pts
print("Estimated value of pi =", pi_est)
plt.scatter(in_x, in_y,
            color="red", s=10, alpha=0.8,
            label="Inside sphere")
plt.scatter(out_x, out_y,
            color="blue", s=10,
            label="Outside sphere")
plt.axis("square")
plt.title("Monte Carlo Simulation for pi estimation")
plt.legend()
plt.show()