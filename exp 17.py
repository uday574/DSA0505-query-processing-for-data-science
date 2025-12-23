import pandas as pd

# Creating the sample student dataset as seen in the images
data = {
    'school': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# 17. Write a Pandas program to split the following dataframe by school code
# and get mean, min, and max value of age for each school.
result = df.groupby('school').agg({'age': ['mean', 'min', 'max']})

print("Original DataFrame:")
print(df)
print("\nMean, min, and max value of age for each school:")
print(result)