from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Static Image OCR
image = Image.open("testocr.png")
ocr = pytesseract.image_to_string(image=image)
print(ocr)

# Real-Time OCR
"""
cv2 to grab video frames continuously;
while grabbing the frames
"""