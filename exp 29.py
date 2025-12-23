import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Defining a list of different colors for each bar
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']

# Create the bar chart with different colors
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()