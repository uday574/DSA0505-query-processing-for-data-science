import numpy as np
import matplotlib.pyplot as plt

# Sample data
groups = 5
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)

# Create plot
fig, ax = plt.subplots()
index = np.arange(groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_men, bar_width,
alpha=opacity,
color='g',
label='Men')

rects2 = plt.bar(index + bar_width, means_women, bar_width,
alpha=opacity,
color='r',
label='Women')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()