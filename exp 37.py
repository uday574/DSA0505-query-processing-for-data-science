import pandas as pd

# Sample dictionary data
data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)