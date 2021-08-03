import numpy as np 
import cv2 

#display video / capture device
#cap = cv2.VideoCapture('sample-mp4-file.mp4')
# put the number of the webcam or video device you want to use (0 would access 1 camera, 1 would access 2 and so on)

#while True:
    #ret, frame = cap.read() #frame or image itself 
    # ret tells you if the capture actually worked properly


    #cv2.imshow('frame', frame)

    #if cv2.waitKey(1) == ord('q'): #cv2.waitKey waits (1) millisecond to push a key and returns the value associated with the key we pressed
        #break

#cap.release() # releases the camera resource so another camera resource can be used
#cv2.destroyAllWindows()

######################################################################################################################################################

#display video / capture device 
cap = cv2.VideoCapture('sample-mp4-file.mp4')
# put the number of the webcam or video device you want to use (0 would access 1 camera, 1 would access 2 and so on)

while True:
    ret, frame = cap.read() #frame or image itself 
    # ret tells you if the capture actually worked properly

    #get the width and height of the video camera
    width = int(cap.get(3)) # cap.get(3) will give you the width of your video capture
    height = int(cap.get(4))

    # turn frame into four separate images or Mirroring video multiple times
    image = np.zeros(frame.shape, np.uint8) #unassigned integer of 8 bits = np.uint8
    #resize frame to fit four images on the canvas
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame #taking this image and putting it in the top left corner of the frame
    image[height//2:, :width//2] = smaller_frame #Bottom left
    image[:height//2, width//2:] = smaller_frame #top right
    image[height//2:, width//2:] = smaller_frame 

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #cv2.waitKey waits (1) millisecond to push a key and returns the value associated with the key we pressed
        break

cap.release() # releases the camera resource so another camera resource can be used
cv2.destroyAllWindows()

########################################################################################################################################################

#display video / capture device 
cap = cv2.VideoCapture('sample-mp4-file.mp4')
# put the number of the webcam or video device you want to use (0 would access 1 camera, 1 would access 2 and so on)

while True:
    ret, frame = cap.read() #frame or image itself 
    # ret tells you if the capture actually worked properly

    #get the width and height of the video camera
    width = int(cap.get(3)) # cap.get(3) will give you the width of your video capture
    height = int(cap.get(4))

    # turn frame into four separate images or Mirroring video multiple times
    image = np.zeros(frame.shape, np.uint8) #unassigned integer of 8 bits = np.uint8
    #resize frame to fit four images on the canvas
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #taking this image and putting it in the top left corner of the frame
    image[height//2:, :width//2] = smaller_frame #Bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #top right
    image[height//2:, width//2:] = smaller_frame 

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #cv2.waitKey waits (1) millisecond to push a key and returns the value associated with the key we pressed
        break

cap.release() # releases the camera resource so another camera resource can be used
cv2.destroyAllWindows()