# Write to Excel
from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
ws = wb.active

# Write data
ws['A1'] = "Test Case ID"
ws['B1'] = "Result"

ws['A2'] = "TC001"
ws['B2'] = "Pass"

# Save to file
wb.save("writeExcel.xlsx")