import pandas as pd

# Sample data
data = [
    {"name": "John Doe", "age": 30, "contribution": 1000},
    {"name": "Jane Smith", "age": 25, "contribution": 2000},
]

df = pd.DataFrame(data)

# Write to Excel file
with pd.ExcelWriter('Federal_Election_Commission_Data.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1')

print("Excel file created successfully!")
