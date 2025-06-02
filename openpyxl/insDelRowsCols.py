# Inserting and deleting rows and columns in Excel

# Import Workbook class from openpyxl
# This allows you to create, read, and modify Excel files
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created automatically)
sheet = wb.active

# Add sample data into cells
# Fill 5 rows (1 to 5), 3 columns (1 to 3) with values like "R1C1", "R1C2", etc.
for i in range(1, 6):           # Loop through row numbers 1 to 5
    for j in range(1, 4):       # Loop through column numbers 1 to 3
        # Set cell value at row=i, column=j
        sheet.cell(row=i, column=j, value=f"R{i}C{j}")

# Insert a single empty row at position 2
# All rows starting from row 2 will be shifted down by 1
sheet.insert_rows(2)

# Insert multiple rows: insert 3 rows starting at row 5
# Rows 5, 6, 7 will now be blank; original data shifts down
sheet.insert_rows(5, 3)

# Insert a single empty column at position 2 (column B)
# Column B and all columns to its right will shift right by 1
sheet.insert_cols(2)

# Delete 2 rows starting from row 7
# This removes rows 7 and 8 (if they existed), shifting up remaining rows
sheet.delete_rows(7, 2)

# Delete column at position 3 (i.e., column C)
# Column C and all to the right will be removed
sheet.delete_cols(3)

# Save the modified workbook to a file named "insDelRowsCols.xlsx"
wb.save("insDelRowsCols.xlsx")