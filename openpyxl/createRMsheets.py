# Creating and removing sheets

from openpyxl import Workbook

wb = Workbook()

# Create new sheets
wb.create_sheet("Data")
wb.create_sheet("Summary", 0)  # Add at the beginning

# Remove a sheet
wb.remove(wb["Sheet"])  # Remove the default sheet

print(wb.sheetnames)  # ['Summary', 'Data']

wb.save("createRMsheets.xlsx")