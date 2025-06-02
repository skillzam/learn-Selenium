# Append data dynamically to an Excel worksheet

# Import Workbook class from openpyxl
# This allows us to create and manipulate Excel files
from openpyxl import Workbook

# Create a new Excel workbook
# A new workbook automatically contains one worksheet
wb = Workbook()

# Get the active worksheet (the default worksheet created with the workbook)
sheet = wb.active

# Add header row using append()
# The append() method adds a row at the end of the current worksheet
sheet.append(["Date", "Product", "Quantity", "Price"])

# Define sample sales data as a list of lists
# Each inner list represents a row of data
sales_data = [
    ["2025-04-01", "Laptop", 5, 1200],
    ["2025-04-01", "Mouse", 10, 25],
    ["2025-04-02", "Monitor", 3, 350]
]

# Loop through each row in the sales_data list
for row in sales_data:
    # Append each row to the worksheet
    sheet.append(row)

# Save the workbook to a file named "appendData.xlsx"
# All appended rows will be saved in this file
wb.save("appendData.xlsx")