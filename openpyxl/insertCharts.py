# Insert charts

# Import Workbook class from openpyxl to create an Excel file
from openpyxl import Workbook

# Import chart types (BarChart, LineChart) and Reference to define data ranges
from openpyxl.chart import BarChart, LineChart, Reference

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet (default sheet created automatically)
sheet = wb.active

# Define sample data: months and corresponding sales values
months = ["Jan", "Feb", "Mar", "Apr", "May"]
values = [30, 45, 37, 50, 62]

# Write month and value into columns A and B respectively
# Loop through both lists simultaneously using enumerate(zip(...), start=1)
for i, (month, value) in enumerate(zip(months, values), start=1):
    # Write month into column 1 (A), row i
    sheet.cell(row=i, column=1, value=month)
    
    # Write value into column 2 (B), row i
    sheet.cell(row=i, column=2, value=value)

# Create a bar chart object
bar_chart = BarChart()

# Set title and axis labels for the bar chart
bar_chart.title = "Monthly Sales"
bar_chart.x_axis.title = "Month"
bar_chart.y_axis.title = "Sales"

# Define the data range for the chart:
# Reference column 2 (sales values), rows 1 to 5
data = Reference(sheet, min_col=2, min_row=1, max_row=5)

# Define categories (X-axis labels): reference column 1 (months), rows 1 to 5
categories = Reference(sheet, min_col=1, min_row=1, max_row=5)

# Add the data to the bar chart
bar_chart.add_data(data)

# Set the categories (X-axis labels) for the bar chart
bar_chart.set_categories(categories)

# Insert the bar chart into the worksheet at cell D1
sheet.add_chart(bar_chart, "D1")

# Create a line chart object
line_chart = LineChart()

# Set title for the line chart
line_chart.title = "Monthly Sales Trend"

# Reuse the same data and categories as the bar chart
line_chart.add_data(data)
line_chart.set_categories(categories)

# Insert the line chart into the worksheet at cell D15
sheet.add_chart(line_chart, "D15")

# Save the workbook to a file named "insertCharts.xlsx"
wb.save("insertCharts.xlsx")