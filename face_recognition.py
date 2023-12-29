import cv2
import time 
class Recognise:
    def __init__(self) -> None:
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainer.yml')
        self.cascadePath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + self.cascadePath
        )
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        #initiate id counter
        self.id = 0

        # names related to ids: example ==> Marcelo: id=1,  etc
        self.names = ['None', 'Ozair', "Sultana"] 

        # Initialize and start realtime video capture
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640) # set video widht
        self.cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        self.minW = 0.1*self.cam.get(3)
        self.minH = 0.1*self.cam.get(4)

    def is_person(self, user_input):
        while True:
            ret, img =self.cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            faces = self.faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(self.minW), int(self.minH)),
            )
            for(x,y,w,h) in faces:
                print((x,y,w,h))
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])
                print(id, confidence)
                # If confidence is less them 100 ==> "0" : perfect match 
                if (confidence < 100):
                    id = self.names[id]
                    confidence = f"{round(confidence,1)}%"
                else:
                    id = "unknown"
                    confidence = f"{round(confidence,1)}%"
                
                # cv2.putText(
                #             img, 
                #             str(id), 
                #             (x+5,y-5), 
                #             self.font, 
                #             1, 
                #             (255,255,255), 
                #             2
                #         )
                # cv2.putText(
                #             img, 
                #             str(confidence), 
                #             (x+5,y+h-5), 
                #             self.font, 
                #             1, 
                #             (255,255,0), 
                #             1
                #         )
                if id == user_input:
                    cv2.putText(
                            img, 
                            str(f"Welcome {id.lower()}"), 
                            (x+5,y-5), 
                            self.font, 
                            1, 
                            (255,255,255), 
                            2
                        )
                    cv2.putText(img, 
                                "Successful Login\nPress N to exit",
                                org=(x - 100, y - 130),
                                fontFace=self.font,
                                fontScale=1, 
                                color=(67,192,67),
                                thickness=2)
                else:
                    break

            cv2.imshow('camera',img) 
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            
            if k == 27:
                break
            elif k == 110:
                break
            

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        self.cam.release()
        cv2.destroyAllWindows()