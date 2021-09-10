import numpy as np 
import cv2

cap = cv2.VideoCapture('sample-mp4-file.mp4')

# extract colors from an image using mask

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #convert image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define colors we want to extract from the image (lower & upper bound)
    lower_blue = np.array([90, 50, 50]) #light blue    
    upper_blue = np.array([130, 255, 255]) #darker blue
                #use hsv colorpicker

    #create a mask => portion of an img or frame
    mask = cv2.inRange(hsv, lower_blue, upper_blue) 
    # => returns a new mask of an img that only shows colors in the range provided; anything else will be black

    result = cv2.bitwise_and(frame, frame, mask=mask) 

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#convert to hsv color of choice
# BGR_color = np.array([[[255, 0, 0]]])
                    #create img w/ 1 pixel
# x = cv2.cvtColor([[[255, 0, 0]]], cv2.COLOR_BGR2HSV)
# x[0][0]