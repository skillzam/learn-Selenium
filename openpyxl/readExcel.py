# Read from Excel

from openpyxl import load_workbook

# Load the workbook
wb = load_workbook("test_data.xlsx")

# Select active worksheet
ws = wb.active

# Read value from cell A1
print(ws['B2'].value)