import matplotlib.pyplot as plt
import numpy as np

# Generating random distributions for X and Y
x = np.random.randn(50)
y = np.random.randn(50)

# Creating the scatter plot with empty circles
# 'facecolors='none'' makes the circles empty, and 'edgecolors' sets the border color
plt.scatter(x, y, s=80, facecolors='none', edgecolors='blue')

# Adding labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot with empty circles")

# Displaying the plot
plt.show()