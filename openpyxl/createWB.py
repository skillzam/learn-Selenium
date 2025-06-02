# Create a workbook and write basic data

from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active

# Rename the sheet
sheet.title = "Data"

# Write values to cells
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "City"

# Add data
data = [
    ["Nikhil", 25, "Belagavi"],
    ["Sandeep", 30, "Bagalkote"],
    ["Azhar", 31, "Mudhol"]
]

for row_idx, row_data in enumerate(data, start=2):
    for col_idx, cell_value in enumerate(row_data, start=1):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)

# Save the workbook
wb.save("student_data.xlsx")