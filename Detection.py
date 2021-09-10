import numpy as np 
import cv2

cap = cv2.VideoCapture('sample-mp4-file.mp4')
#HAAR CASCADE => Already trained to look at an image & can pick out certain features in that image 
#load HAAR CASCADE
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    # Face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                    #| how accurate does the algo have to be at detection faces & eyes (min neighbors)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                                                #| reduces image size (scale factor)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        #find the face
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()