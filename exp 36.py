import matplotlib.pyplot as plt
import numpy as np

# Generating sample data for three groups
# Group 1
weight1 = np.random.normal(50, 5, 20)
height1 = np.random.normal(155, 10, 20)

# Group 2
weight2 = np.random.normal(70, 8, 20)
height2 = np.random.normal(175, 12, 20)

# Group 3
weight3 = np.random.normal(90, 10, 20)
height3 = np.random.normal(185, 8, 20)

# Plotting the three groups
plt.scatter(weight1, height1, color='red', label='Group 1')
plt.scatter(weight2, height2, color='blue', label='Group 2')
plt.scatter(weight3, height3, color='green', label='Group 3')

# Adding labels and title
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Group-wise Weight vs Height Comparison')

# Displaying the legend
plt.legend()

# Showing the plot
plt.show()