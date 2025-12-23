import pandas as pd
import matplotlib.pyplot as plt

# Data derived from the provided Alphabet Inc. stock table (image_95848f.png)
data = {
    'Date': ['01-04-2020', '02-04-2020', '03-04-2020', '06-04-2020', '07-04-2020',
             '08-04-2020', '09-04-2020', '13-04-2020', '14-04-2020', '15-04-2020',
             '16-04-2020', '17-04-2020', '20-04-2020', '21-04-2020', '22-04-2020',
             '23-04-2020', '24-04-2020', '27-04-2020', '28-04-2020', '29-04-2020',
             '30-04-2020', '01-05-2020'],
    'Open': [1122, 1098.26, 1119.015, 1138, 1221, 1206.5, 1224.08, 1209.18,
             1245.09, 1245.61, 1274.1, 1284.85, 1271, 1247, 1245.54, 1271.55,
             1261.17, 1296, 1287.93, 1341.46, 1324.88, 1328.5],
    'High': [1129.69, 1126.86, 1123.54, 1194.66, 1225, 1219.07, 1225.57, 1220.51,
             1282.07, 1280.46, 1279, 1294.43, 1281.6, 1254.27, 1285.613, 1293.31,
             1280.4, 1296.15, 1288.05, 1359.99, 1352.82, 1352.07],
    'Low': [1097.45, 1096.4, 1079.81, 1130.94, 1182.23, 1188.16, 1196.735, 1187.598,
            1236.93, 1240.4, 1242.62, 1271.23, 1261.37, 1209.71, 1242, 1265.67,
            1249.45, 1269, 1232.2, 1325.34, 1322.49, 1311],
    'Close': [1105.62, 1120.84, 1097.88, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56,
              1269.23, 1262.47, 1263.47, 1283.25, 1266.61, 1216.34, 1263.21, 1276.31,
              1279.31, 1275.88, 1233.67, 1341.48, 1348.66, 1320.61]
}

df = pd.DataFrame(data)

# Convert the Date column to datetime objects for correct plotting
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Set the Date as the index
df.set_index('Date', inplace=True)

# Generate a line chart for the financial data (Open, High, Low, Close)
df[['Open', 'High', 'Low', 'Close']].plot(figsize=(10, 6))

# Add labels, title, and grid
plt.title('Alphabet Inc. Stock Financial Data (April 2020)')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.grid(True)
plt.legend(loc='best')

# Display the chart
plt.tight_layout()
plt.show()