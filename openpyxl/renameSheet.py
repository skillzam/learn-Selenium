# Purpose: Rename the default sheet in an Excel workbook

# Import the Workbook class from openpyxl
# This allows you to create, read, and write Excel files
from openpyxl import Workbook

# Create a new Excel workbook
# This automatically includes one default worksheet
wb = Workbook()

# Get the active (default) worksheet
# This is the first (and only) sheet created when the workbook was initialized
sheet = wb.active

# Rename the worksheet's title to "Sales_Report"
sheet.title = "Sales_Report"

# Save the workbook to a file named "renameSheet.xlsx"
# The renamed sheet will be saved in this file
wb.save("renameSheet.xlsx")