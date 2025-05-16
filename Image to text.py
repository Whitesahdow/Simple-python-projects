#first we need to install tesseract from  https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
from PIL import Image

# Path to your installed tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    # Load the image
    img = Image.open(r'Images\motivation.jpg')

    # Convert to grayscale since it may not catch texts in different colors
    gray = img.convert("L")

    # Apply basic threshold to increase contrast
    threshold = 150
    bw = gray.point(lambda x: 255 if x > threshold else 0) # type: ignore

    # OCR
    text = pytesseract.image_to_string(bw)

    print("_________________________the text is ___________\n",text)

convert()
