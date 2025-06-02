# Conditional formatting allows you to apply styles based on cell values
# Creates an Excel file with sample data in cells A1 to D10.
# Applies two types of conditional formatting :
# A color scale gradient from green (low) to red (high), with yellow at the midpoint.
# A custom rule that highlights cells with values less than 5 with red text and light red background.


# Import necessary modules from openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill  # For styling fonts and fills
from openpyxl.styles.differential import DifferentialStyle  # For defining style differences used in rules
from openpyxl.formatting.rule import Rule, ColorScaleRule  # For creating conditional formatting rules

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created with the workbook)
sheet = wb.active

# Add sample numeric data into cells A1:D10
for row in range(1, 11):  # Loop through rows 1 to 10
    for col in range(1, 5):  # Loop through columns 1 to 4 (A-D)
        # Fill each cell with a calculated value: (row-1)*4 + col
        sheet.cell(row=row, column=col, value=(row-1)*4 + col)

# Define a color scale rule: green (low) -> yellow (mid) -> red (high)
color_scale = ColorScaleRule(
    start_type="min", start_color="63BE7B",  # Green for lowest values
    mid_type="percentile", mid_value=50, mid_color="FFEB84",  # Yellow for 50th percentile
    end_type="max", end_color="F8696B"  # Red for highest values
)

# Apply the color scale to the range A1:D10
sheet.conditional_formatting.add("A1:D10", color_scale)

# Define a font style for values less than 5 (red text)
red_text = Font(color="FF0000")  # Red text

# Define a fill style for values less than 5 (light red background)
red_fill = PatternFill(start_color="FFCCCC", end_color="FFCCCC", fill_type="solid")  # Light red fill

# Combine font and fill into a differential style (used in conditional rules)
dxf = DifferentialStyle(font=red_text, fill=red_fill)

# Create a rule that applies when a cell's value is less than 5
rule = Rule(
    type="cellIs",                  # Type of rule: "cellIs" for comparisons like less than, greater than
    operator="lessThan",            # Apply if value < 5
    formula=["5"],                  # Threshold value for comparison
    dxf=dxf                         # Style to apply if condition is met
)

# Apply this rule to the range A1:D10
sheet.conditional_formatting.add("A1:D10", rule)

# Save the workbook to a file named "condFormat.xlsx"
wb.save("condFormat.xlsx")