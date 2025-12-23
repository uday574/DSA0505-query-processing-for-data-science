import numpy as np
import matplotlib.pyplot as plt

# Sample Data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)

ind = np.arange(5)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

# Create men's bars
p1 = ax.bar(ind, men_means, width, yerr=men_std, label='Men')

# Create women's bars stacked on top of men's bars using 'bottom'
p2 = ax.bar(ind, women_means, width, bottom=men_means, yerr=women_std, label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()

plt.show()