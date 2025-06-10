# Convert to Python data structures

from openpyxl import load_workbook

# Function to convert worksheet data to list of dictionaries
def sheet_to_dict(sheet):
    data = []
    
    # Get headers from the first row
    if sheet.max_row < 1:
        return data  # Return empty list if no rows
    
    headers = [cell.value if cell.value is not None else f"col_{i}" 
               for i, cell in enumerate(sheet[1])]
    print("Headers", len(headers))

    # Iterate through data rows
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}
        for key, value in zip(headers, row):
            row_data[key] = value
        data.append(row_data)
    
    return data

# --- Example Usage ---
wb = load_workbook("test_data.xlsx")   
sheet = wb.active

data_dict = sheet_to_dict(sheet)

# print("data_dict", data_dict)

for row in data_dict:
    print(row)