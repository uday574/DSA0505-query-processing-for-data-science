import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'name_code': ['Company_001', 'Company_002', 'Firm_003', 'Agency_004']
})

# Substring to find
substring = '003'

# Find the index where the substring exists in the column
# We use str.contains() to find rows, and then get the index
result_index = df.index[df['name_code'].str.contains(substring)].tolist()

print(f"The substring '{substring}' was found at index: {result_index}")