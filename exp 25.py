import matplotlib.pyplot as plt

# Data for the lines
x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]

# Plotting the lines with different colors and widths
plt.plot(x, y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x, y2, color='red', linewidth=5, label='line2-width-5')

# Adding labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines with different widths and colors with suitable legends')

# Displaying the legend
plt.legend()

# Showing the plot
plt.show()