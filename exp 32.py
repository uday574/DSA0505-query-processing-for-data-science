import matplotlib.pyplot as plt
from pylab import randn

# Generating random distributions for X and Y
X = randn(200)
Y = randn(200)

# Creating the scatter plot
plt.scatter(X, Y, color='r')

# Adding labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot of random distribution")

# Displaying the plot
plt.show()