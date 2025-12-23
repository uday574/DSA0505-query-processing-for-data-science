import pandas as pd
import numpy as np

# Create a dataframe of ten rows and four columns with random values
np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 4), columns=['B', 'C', 'D', 'E'])

# Insert column 'A' with values 1 to 10
df.insert(0, 'A', range(1, 11))

# Manually insert NaN values to match the visual provided in the context
df.iloc[0, 2] = np.nan
df.iloc[3, 3] = np.nan
df.iloc[4, 1] = np.nan
df.iloc[9, 4] = np.nan

# Function to apply black background and yellow font for terminal output
def apply_theme(val):
    # ANSI escape codes: \033[40m for black background, \033[33m for yellow text
    theme = "\033[40;33m"
    reset = "\033[0m"
    if pd.isna(val):
        return f"{theme}{'nan':>10}{reset}"
    return f"{theme}{val:10.6f}{reset}"

# Print the header
print(f"{'':>3} {'A':>3} {'B':>10} {'C':>10} {'D':>10} {'E':>10}")

# Print rows with theme logic
for i, row in df.iterrows():
    formatted_row = [f"{int(row['A']):>3}"]
    for col in ['B', 'C', 'D', 'E']:
        formatted_row.append(apply_theme(row[col]))
    print(f"{i:>3} " + " ".join(formatted_row))

# Note: In a Jupyter Notebook with jinja2 installed, you would use:
# df.style.set_properties(**{'background-color': 'black', 'color': 'yellow'})