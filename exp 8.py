import pandas as pd

# Sample sales data
data = {
    'Item': ['Television', 'Television', 'Home Theater', 'Home Theater', 'Television', 'Home Theater', 'Television', 'Home Theater'],
    'Units': [15, 10, 8, 12, 5, 7, 11, 9],
    'Sale_Amt': [1200, 1500, 800, 700, 1100, 900, 1300, 750]
}

sales_data = pd.DataFrame(data)

# Create Pivot table to find item wise unit sold
pivot_table = pd.pivot_table(sales_data, index='Item', values='Units', aggfunc='sum')

print(pivot_table)