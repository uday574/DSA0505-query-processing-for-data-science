import matplotlib.pyplot as plt

# Define the data points for the line
x = [1, 2, 3, 49]
y = [3, 6, 9, 147] # Example values to match the linear trend in the image

# Plotting the line
plt.plot(x, y, color='blue', linewidth=1)

# Set the x-axis label
plt.xlabel('x - axis')

# Set the y-axis label
plt.ylabel('y - axis')

# Set the title of the graph
plt.title('Draw a line.')

# Set the axis limits to match the image style
plt.xlim(0, 50)
plt.ylim(0, 160)

# Display the plot
plt.show()