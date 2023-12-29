import cv2
import os
import time

cap = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
def detect_bounding_box(vid, count):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    print(f"length of faces:{len(faces)}")
    
    for (x, y, w, h) in faces:
        print((x, y, w, h))
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        count += 1
        filename = "face_images"
        if not os.path.exists(filename):
            os.makedirs(filename, exist_ok=True)
        
        cv2.imwrite(filename=f"{filename}/Sultana.2.{str(count)}.jpg", img= gray_image[y:y+h,x:x+w])
        time.sleep(1)
    return faces, count

# call function to detect face
print("Calling function for detecting face")
if not cap.isOpened():
    raise IOError("Cannot open webcam")

count = 0
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    print(frame.shape)
    face, count = detect_bounding_box(frame, count)
    print(count)
    cv2.imshow('Input', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
    if count == 30:
        break