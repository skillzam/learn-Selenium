# Modify existing Excel files

from openpyxl import load_workbook

# Load an existing workbook
wb = load_workbook("student_data.xlsx")
sheet = wb.active

# Modify cell values
sheet["B3"] = 27
sheet["D1"] = "Status"
sheet.cell(row=3, column=4).value = "Modified"

# Save to a new file (to preserve the original)
wb.save("new_student_data.xlsx")