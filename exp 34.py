import math
import random
import matplotlib.pyplot as plt

# Generating random data for the scatter plot
no_of_balls = 25
x = [random.triangular() for _ in range(no_of_balls)]
y = [random.gauss(0.5, 0.25) for _ in range(no_of_balls)]
# Random sizes for the 'balls'
colors = [random.randint(1, 4) for _ in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for _ in range(no_of_balls)]

# Create the scatter plot
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)

# Adding labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot with balls of different sizes")

# Displaying the plot
plt.show()