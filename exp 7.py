import pandas as pd

# Creating the sales_data DataFrame based on typical sales record structures
data = {
    'Region': ['East', 'West', 'East', 'West', 'East', 'West', 'East', 'West'],
    'Item': ['Television', 'Television', 'Home Theater', 'Home Theater', 'Television', 'Home Theater', 'Television', 'Home Theater'],
    'Sale_Amt': [1200, 1500, 800, 700, 1100, 900, 1300, 750]
}

sales_data = pd.DataFrame(data)

# Create Pivot table to find maximum and minimum sale value for each item
pivot_table = pd.pivot_table(sales_data, values='Sale_Amt', index=['Item'], aggfunc={'Sale_Amt': ['max', 'min']})

print(pivot_table)