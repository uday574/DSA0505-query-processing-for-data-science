import pandas as pd
import numpy as np

# Create a dataframe of ten rows and four columns with random values
np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 4), columns=['B', 'C', 'D', 'E'])

# Insert column 'A' with values 1 to 10
df.insert(0, 'A', range(1, 11))

# Convert some specific values to NaN as per the image example
df.iloc[0, 2] = np.nan  # Row 0, Col C
df.iloc[3, 3] = np.nan  # Row 3, Col D
df.iloc[4, 1] = np.nan  # Row 4, Col B
df.iloc[9, 4] = np.nan  # Row 9, Col E

# Function to highlight NaN values in red background for terminal output
def highlight_nan(val):
    if pd.isna(val):
        return f"\033[41m{'nan':>10}\033[0m"
    return f"{val:10.6f}"

# Print the header
print(f"{'':>3} {'A':>3} {'B':>10} {'C':>10} {'D':>10} {'E':>10}")

# Print rows with highlighting logic
for i, row in df.iterrows():
    formatted_row = [f"{int(row['A']):>3}"]
    for col in ['B', 'C', 'D', 'E']:
        formatted_row.append(highlight_nan(row[col]))
    print(f"{i:>3} " + " ".join(formatted_row))

# Note: In a Jupyter Notebook with jinja2 installed, you would use:
# df.style.highlight_null(null_color='red')