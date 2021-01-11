# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

filepdf = str(sys.argv[1])

if os.path.exists(filepdf):
    # Increase DPI (300) if image quality is too poor
    images = convert_from_path(filepdf, 300)
    # i counts each page
    i = 1

    # Process each page as image
    for image in images:
        filename = "pdfimage"+str(i)+".jpg"
        image.save(filename, 'JPEG')
        i = i + 1

    # Output file name, should be the same as pdf but with txt extension.
    outfile = "out_text.txt"

    # Open the target file
    f = open(outfile, "a")

    # Iterate from 1 to total number of pages
    # Read each img text and append it to document
    for i in range(1, i):
        readimage = Image.open("pdfimage"+str(i)+".jpg")
        text = str(((pytesseract.image_to_string(readimage))))
        f.write(text)
        # remove the processed image
        if os.path.exists("pdfimage"+str(i)+".jpg"):
            os.remove("pdfimage"+str(i)+".jpg")

    # Close file
    f.close()

    print(outfile)
else:
    print("Argument is not a valid filename")
