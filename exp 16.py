import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# [cite_start]Sample data for the student dataframe [cite: 738]
data = {
    'school': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# [cite_start]16. Split the dataframe into groups based on school code [cite: 736]
grouped_data = df.groupby('school')

# [cite_start]Plotting the average height per school based on grouped data [cite: 823]
grouped_data['height'].mean().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.title('Average Height per School')
plt.xlabel('School Code')
plt.ylabel('Mean Height')
plt.savefig('school_plot.png')

# Displaying groups
for name, group in grouped_data:
    print(f"Group: {name}")
    print(group)
    print("-" * 30)

# [cite_start]Check and print the type of the GroupBy object [cite: 737]
print("\nType of GroupBy object:")
print(type(grouped_data))