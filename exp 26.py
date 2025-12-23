import matplotlib.pyplot as plt

# Data for the first plot
x1 = [10, 20, 30]
y1 = [20, 40, 10]

# Data for the second plot
x2 = [10, 20, 30]
y2 = [40, 10, 30]

# Create a figure with two subplots (1 row, 2 columns)
plt.figure(figsize=(10, 4))

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'b-')
plt.title('Plot 1')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'r-')
plt.title('Plot 2')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()