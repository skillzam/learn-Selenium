# Copying worksheets

from openpyxl import Workbook

wb = Workbook()
source = wb.active
source.title = "Original"

# Add some data to copy
source["A1"] = "Test Data"

# Create a copy
wb.copy_worksheet(source)

# The copied sheet will have "Copy of Original" name
wb.save("copySheet.xlsx")