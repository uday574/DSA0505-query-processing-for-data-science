import pandas as pd
import numpy as np

# Creating the DataFrame based on the provided table in image_95f189.png
data = {
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, "--", 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, "?", 12.43, 2480.4, 250.45, 3045.6],
    'ord_date': ["?", '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, "--", 3002, 3001, 3001],
    'salesman_id': [5002, 5003, "?", 5001, np.nan, 5002, 5001, "?", 5003, 5002, 5003, "--"]
}

df = pd.DataFrame(data)

# 14. Write a Pandas program to find and replace the missing values in a given
# DataFrame which do not have any valuable information.
# We replace common placeholders like '?' and '--' with NaN
result = df.replace(['?', '--'], np.nan)

print("Original DataFrame:")
print(df)
print("\nDataFrame after replacing '?' and '--' with NaN:")
print(result)