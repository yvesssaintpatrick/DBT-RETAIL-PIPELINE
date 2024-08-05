import pandas as pd

# Attempt to read the CSV file with a likely encoding
try:
    df = pd.read_csv('include/dataset/online_retail.csv', encoding='ISO-8859-1')
except UnicodeDecodeError:
    df = pd.read_csv('include/dataset/online_retail.csv', encoding='windows-1252')

# Print the first few rows to verify data integrity
print(df.head())

# Save the DataFrame to a new CSV file with UTF-8 encoding
df.to_csv('include/dataset/online_retail_fixed.csv', index=False, encoding='utf-8')
