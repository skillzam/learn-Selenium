# openpyxl 

## It is a Python library used to read from and write to Excel files (specifically .xlsx files). It allows you to automate tasks like:

## openpyxl documentation `https://openpyxl.readthedocs.io/en/stable/`
## Source code `https://foss.heptapod.net/openpyxl/openpyxl`

1. Reading data from Excel
2. Updating or writing new data into Excel
3. Formatting cells, rows, columns
4. Creating new sheets, renaming them, deleting them
5. Applying styles, colors, formulas, etc.

It works with Microsoft Office Open XML (OOXML) format, which is the default for modern Excel files (xlsx), but does not support older xls files.he library works with several file formats:
 1. .xlsx - Excel workbook
 2. .xlsm - Excel workbook with macros
 3. .xltx - Excel template
 4. .xltm - Excel template with macros

# Why Use openpyxl?
If you're doing test automation using Selenium or any other framework and want to:

1. Read test data from an Excel file (data-driven testing)
2. Write results/status back to Excel

Then openpyxl is a great choice!

# Installation

`pip install openpyxl`

# Common Operations with `openpyxl`


| Action               | Code Example                                  |
|----------------------|-----------------------------------------------|
| Load Excel File      | `wb = load_workbook('file.xlsx')`             |
| Get Active Sheet     | `ws = wb.active`                              |
| Access Cell Value    | `ws['A1'].value`                              |
| Update Cell Value    | `ws['A1'] = 'New Value'`                      |
| Save Changes         | `wb.save('file.xlsx')`                        |
| Get All Rows         | `for row in ws.iter_rows(): ...`              |


# Key Concepts and Terminology
To use openpyxl effectively, you need to understand the basic Excel structure:

1. Workbook: The Excel file itself, containing one or more worksheets
2. Worksheet: Individual tabs/sheets within a workbook
3. Cell: Individual data points in a worksheet, identified by column letter and row number (e.g., “A1”)
4. Row: Horizontal line of cells, identified by numbers (1, 2, 3...)
5. Column: Vertical line of cells, identified by letters (A, B, C...)

In openpyxl, you can reference cells using either:

1. Excel style references: sheet[“A1”]
2. Row-column indexing: sheet.cell(row=1, column=1) (Note: openpyxl uses 1-based indexing, not 0-based)


# Pillow Library
Pillow is a Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats. It’s one of the most commonly used libraries in Python for working with images.

## Installation `pip install pillow`

## What Can Pillow Do?
Pillow allows you to perform a wide range of image processing tasks , such as:

| Operation               | Description                                 |
|-------------------------|---------------------------------------------|
| Open and display images | View images in code or GUI apps             |
| Resize images           | Make thumbnails or responsive images        |
| Crop, rotate, flip      | Edit images programmatically                |
| Filter and enhance      | Apply blur, sharpen, contrast, etc.         |
| Draw on images          | Add text, shapes, watermarks                |
| Convert between formats | PNG → JPEG, etc.                            |
| Extract metadata        | Read EXIF data from photos                  |

## Why You Might Need Pillow with `openpyxl` ?
When using openpyxl to insert images into Excel files (like in your earlier example), Pillow is required because:

1. openpyxl uses Pillow internally to load and process images (.png, .jpg, etc.)
2. Without Pillow installed, you’ll get an error like:
`NotImplementedError: image file not loaded: install Pillow?`

## Documentation
https://pillow.readthedocs.io

