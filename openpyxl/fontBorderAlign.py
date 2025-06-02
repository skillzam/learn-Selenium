# Import necessary modules from openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, NamedStyle

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created with the workbook)
sheet = wb.active

# Define a reusable style called "header_style" for styling header cells
header_style = NamedStyle(name="header_style")

# Set font style for the header: bold, size 12, white color (#FFFFFF)
header_style.font = Font(bold=True, size=12, color="FFFFFF")

# Set background fill color for header: solid fill with color #366092 (dark blue)
header_style.fill = PatternFill(fill_type="solid", start_color="366092")

# Center align text horizontally and vertically in header cells
header_style.alignment = Alignment(horizontal="center", vertical="center")

# Add borders to the header cells:
# - Bottom border: medium black line
# - Left, right, top borders: thin lines (default color is black)
header_style.border = Border(
    bottom=Side(border_style="medium", color="000000"),
    left=Side(border_style="thin"),
    right=Side(border_style="thin"),
    top=Side(border_style="thin")
)

# Add this custom style to the workbook so it can be used later
wb.add_named_style(header_style)

# Define headers for the first row of the sheet
headers = ["ID", "Product", "Category", "Price"]

# Loop through each header, write into the first row (row=1), starting at column 1
for col_idx, header in enumerate(headers, start=1):
    # Access cell at row=1 and current column index, set its value to header text
    cell = sheet.cell(row=1, column=col_idx, value=header)
    
    # Apply the named style "header_style" to the cell
    cell.style = "header_style"

# Apply basic styles directly to specific cells without using NamedStyle

# Make text in A2 bold and italic
sheet["A2"].font = Font(bold=True, italic=True)

# Center-align text in A3
sheet["A3"].alignment = Alignment(horizontal="center")

# Add a thin bottom border to A4
sheet["A4"].border = Border(bottom=Side(border_style="thin"))

# Save the workbook to a file named "fontBorderAlign.xlsx"
wb.save("fontBorderAlign.xlsx")