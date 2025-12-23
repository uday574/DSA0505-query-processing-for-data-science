import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Alphabet Inc. (GOOGL) to ensure the code runs without external files
data = {
    'Date': ['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06', '2020-04-07'],
    'Volume': [2343100, 1964900, 2313400, 2664700, 1856700]
}

df = pd.DataFrame(data)

# Convert Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Define specific dates
start_date = '2020-04-01'
end_date = '2020-04-30'

# Filter data between the two dates
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['Date'].dt.strftime('%Y-%m-%d'), filtered_df['Volume'], color='skyblue')
plt.title('Alphabet Inc. Trading Volume (April 2020)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()