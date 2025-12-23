import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Alphabet Inc. (GOOGL) to avoid FileNotFoundError
data = {
    'Date': ['2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-09-30'],
    'Close': [1102.10, 1320.15, 1435.96, 1464.70, 1629.53, 1655.08, 1465.60]
}

df = pd.DataFrame(data)

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Define specific dates
start_date = '2020-04-01'
end_date = '2020-09-30'

# Filter data between the two dates
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df['Close'], marker='o', linestyle='-')
plt.title('Alphabet Inc. Stock Price (Apr 2020 - Sep 2020)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()