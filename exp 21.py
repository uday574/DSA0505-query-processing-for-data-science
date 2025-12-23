import pandas as pd

# Creating a sample DataFrame
data = {
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton'],
    'company_code': ['AbCd', 'eFgH', 'iJkL', 'mNoP']
}
df = pd.DataFrame(data)

# Swapping the cases of the 'company_code' column
df['company_code'] = df['company_code'].str.swapcase()

print("Original DataFrame with swapped cases in 'company_code':")
print(df)