import pandas as pd
import matplotlib.pyplot as plt
import io

# Sample financial data provided in the prompt
csv_data = """Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017"""

# Loading the data into a DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Converting the Date column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Setting the Date column as the index
df.set_index('Date', inplace=True)

# Plotting the financial data
df.plot()

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Financial Data of Alphabet Inc.')

# Displaying the chart
plt.show()