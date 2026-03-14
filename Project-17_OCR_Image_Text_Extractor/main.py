"""
OCR Image Text Extractor

This script reads all JPG images from the 'images' folder,
extracts text from each image using Tesseract OCR, and writes
the extracted text into a file named 'mark_list.txt'.

Libraries used:
- pathlib: For easy file and folder handling
- PIL (Pillow): For image processing
- pytesseract: Python wrapper for Google's Tesseract OCR
"""

from pathlib import Path
from PIL import Image
import pytesseract

# Define the folder path that contains the images
# Using pathlib makes file handling cleaner and cross-platform compatible
folder = Path("images")

# Open the output file in write mode
# If the file already exists, it will be overwritten
with open("file.txt", "w") as file:

    # Iterate through all .jpg images inside the images folder
    # glob("*.jpg") finds files with the .jpg extension
    for image_file in folder.glob("*.jpg"):

        # Open the image file using Pillow
        img = Image.open(image_file)

        # Convert the image to grayscale ("L" mode)
        # This often improves OCR accuracy by removing color noise
        img = img.convert("L")

        # Extract text from the image using Tesseract OCR
        text = pytesseract.image_to_string(img)

        # Write the file name to the output file for reference
        file.write(f"\nFile: {image_file.name}\n")

        # Write the extracted text
        file.write(text + "\n")

        # Add a separator line for better readability between image outputs
        file.write("*" * 50 + "\n")