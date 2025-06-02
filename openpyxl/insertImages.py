# Insert Images into Excel using openpyxl
# Note: You need the Pillow library installed to work with images
#       Install it using: pip install pillow

try:
    # Import Workbook class to create a new Excel file
    from openpyxl import Workbook

    # Import Image class to insert images into worksheet
    from openpyxl.drawing.image import Image

    # Optional: Try importing PIL to give a friendly error if Pillow is missing
    try:
        from PIL import Image as PILImage
    except ImportError:
        raise ImportError("Pillow library not installed. Please install it with: pip install pillow")

    # Create a new Excel workbook
    wb = Workbook()

    # Get the active worksheet (default sheet created automatically)
    sheet = wb.active

    # Load an image from the file system (e.g., image.png)
    # Make sure "image.png" exists in the same directory or provide full path
    img = Image("image.png")

    # Optional: Resize the image to fit better in the worksheet
    # Set width to 150 pixels and height to 75 pixels
    img.width = 150
    img.height = 75

    # Insert the image into the worksheet, anchoring it at cell A1
    sheet.add_image(img, "A1")

    # Save the workbook to a file named "image.xlsx"
    wb.save("image.xlsx")

    print("Image inserted successfully into Excel!")

except Exception as e:
    print(f"Error: {e}")