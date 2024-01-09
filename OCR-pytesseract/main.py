import pytesseract
from pytesseract import Output
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread('mr_code.png')
W, H, C = img.shape

# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# Real-Time OCR
"""
cv2 to grab video frames;
while grabbing the frames
"""


MR_CODE = "12354"
while True:
    d = pytesseract.image_to_boxes(img)
    detection = ""
    for b in d.splitlines():
        print(b)
        b = b.split(" ")
        detection += b[0]
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        
        rect = cv2.rectangle(img, (x, W - y), (w, W - h), (0, 255, 0), 2)
        cv2.imshow('img', rect)
    
    if MR_CODE == detection:
        print(f"Patient Recognized: {detection} == {MR_CODE}")
    
    if cv2.waitKey(0) and 0xFF == ord("q"):
        break
    