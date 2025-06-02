# Adding formulas

# Import the Workbook class from openpyxl to create and manipulate Excel files
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created automatically)
sheet = wb.active

# Add sample numeric data into column A (rows 1 to 5)
for row in range(1, 6):  # Loop from row 1 to 5
    # Write the row number into column 1 (i.e., column A)
    sheet.cell(row=row, column=1, value=row)

# Add formulas in column B and C to perform calculations based on values in column A

# Multiply value in A1 by 2 and display result in B1
sheet["B1"] = "=A1*2"

# Multiply value in A2 by 2 and display result in B2
sheet["B2"] = "=A2*2"

# Calculate the sum of values from A1 to A5 and display result in C1
sheet["C1"] = "=SUM(A1:A5)"

# Calculate the average of values from A1 to A5 and display result in C2
sheet["C2"] = "=AVERAGE(A1:A5)"

# Count how many values in A1:A5 are greater than 2 and display result in C3
sheet["C3"] = "=COUNTIF(A1:A5,\">2\")"

# Save the workbook to a file named "addFormulas.xlsx"
wb.save("addFormulas.xlsx")