import pandas as pd
import numpy as np

# 15. Write a Pandas program to keep the rows with at least 2 NaN values in a given DataFrame.

# Creating the DataFrame based on the provided table in image_95f56c.png
data = {
    'ord_no': [np.nan, np.nan, 70002.0, np.nan, np.nan, 70005.0, np.nan, 70010.0, 70003.0, 70012.0, np.nan, np.nan],
    'purch_amt': [np.nan, 270.65, 65.26, np.nan, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, np.nan],
    'ord_date': [np.nan, '2012-09-10', np.nan, np.nan, '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', np.nan],
    'customer_id': [np.nan, 3001.0, 3001.0, np.nan, 3002.0, 3001.0, 3001.0, 3004.0, 3003.0, 3002.0, 3001.0, np.nan]
}

df = pd.DataFrame(data)

# Logic: Keep rows with at least 2 NaN values
# we count nulls per row and filter where count is >= 2
result = df[df.isnull().sum(axis=1) >= 2]

print("Original DataFrame:")
print(df)
print("\nRows with at least 2 NaN values:")
print(result)