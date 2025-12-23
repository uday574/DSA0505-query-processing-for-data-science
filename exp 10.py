import pandas as pd
import numpy as np

# Create a dataframe of ten rows and four columns with random values
np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 4), columns=['B', 'C', 'D', 'E'])

# Add the index column 'A'
df.insert(0, 'A', range(1, 11))

# Function to apply color formatting to the terminal output
def color_text(val):
    if isinstance(val, (int, float)):
        color = "\033[31m" if val < 0 else "\033[30m"
        return f"{color}{val: .6f}\033[0m"
    return val

# Print the header
print(f"{'':>3} {'A':>3} {'B':>10} {'C':>10} {'D':>10} {'E':>10}")

# Print the rows with color logic for terminal
for i, row in df.iterrows():
    formatted_row = [f"{int(row['A']):>3}"]
    for col in ['B', 'C', 'D', 'E']:
        formatted_row.append(f"{color_text(row[col]):>20}")
    print(f"{i:>3} " + " ".join(formatted_row))