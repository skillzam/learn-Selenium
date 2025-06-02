from openpyxl import load_workbook

# Load the Excel workbook
wb = load_workbook("test_data.xlsx")   

# Select the active worksheet or specify by name: wb["SheetName"]
sheet = wb.active

# --- Iterate through rows ---
print("Iterating through rows:")
for row in sheet.iter_rows(min_row=1, max_row=3, values_only=True):
    print(row)  # Each row is a tuple of cell values

# --- Iterate through columns ---
print("\nIterating through columns:")
for col in sheet.iter_cols(min_col=1, max_col=3, values_only=True):
    print(col)  # Each column is a tuple of cell values

# --- Access a range of cells ---
print("\nAccessing values from A1:C3:")
cell_range = sheet["A1:C3"]
for row in cell_range:
    for cell in row:
        print(cell.value)