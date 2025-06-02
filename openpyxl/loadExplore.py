# Load and explore a workbook

from openpyxl import load_workbook

# Load the workbook - use read_only=True for large files
wb = load_workbook('test_data.xlsx', read_only=False, data_only=False)
# data_only=True reads values instead of formulas

# Select active worksheet
ws = wb.active

print(ws)