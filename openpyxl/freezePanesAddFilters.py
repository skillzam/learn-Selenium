# Freezing panes and adding filters


# Import Workbook class from openpyxl
# This allows you to create, read, and modify Excel files
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created when workbook is initialized)
sheet = wb.active

# Define column headers
headers = ["ID", "Name", "Department", "Salary"]

# Loop through headers and write them into the first row (row=1)
# enumerate starts at 1 because Excel rows/columns are 1-indexed
for col_idx, header in enumerate(headers, start=1):
    # Write each header into cell at row=1, column=col_idx
    sheet.cell(row=1, column=col_idx, value=header)

# Define sample data: list of employee records
data = [
    [1, "Sunil", "HR", 55000],
    [2, "Steve", "IT", 65000],
    [3, "Omer", "Finance", 60000]
]

# Loop through data rows starting at row=2 (below headers)
for row_idx, row_data in enumerate(data, start=2):  # start=2 means row 2 onwards
    # For each row, loop through its values and write to corresponding columns
    for col_idx, value in enumerate(row_data, start=1):  # start=1 for columns A, B, C, D
        sheet.cell(row=row_idx, column=col_idx, value=value)

# Freeze the header row by setting freeze_panes to "A2"
# This means everything above and to the left of A2 will be frozen
sheet.freeze_panes = "A2"

# Set up an auto-filter on the range A1:D4
# This includes headers (row 1) and 3 rows of data (rows 2–4)
sheet.auto_filter.ref = "A1:D4"

# Save the workbook to a file named "freeze_and_filter.xlsx"
wb.save("freezePanesAddFilters.xlsx")