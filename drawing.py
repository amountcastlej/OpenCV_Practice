import numpy as numpy
import cv2

# cap = cv2.VideoCapture('sample-mp4-file.mp4')

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#draw a line                                        color bgr  line thickness
    # img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), (10)) # top left corner to bottom right corner
    # cv2.imshow('frame', img)

# 0, 0 is the top left corner on the x & y axis

    # cv2.imshow('frame', frame)

    # if cv2.waitKey(1) == ord('q'):
    #     break

# cap.release()
# cv2.destroyAllWindows()

#################################################################################################################

# two lines crossing each other to form an x

# cap = cv2.VideoCapture('sample-mp4-file.mp4')

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#draw 2 lines                                       color bgr  line thickness
    # img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), (10)) # top left corner to bottom right corner
    # img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), (5)) # draw other line as a diagonal on the image
    # cv2.imshow('frame', img)

# 0, 0 is the top left corner on the x & y axis

    # cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

################################################################################################################

cap = cv2.VideoCapture('sample-mp4-file.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), (10))
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), (5))
#draw a rectangle                                     #color          # -1 means filled in
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
                            #top left, bottom right corner

# draw a circle      center position  radius  color
    img = cv2.circle(img, (100, 100), 60, (0, 0, 255), 2)

# text
    font = cv2.FONT_HERSHEY_SIMPLEX
                                                #bottom left-hand corner for text         line type
    img = cv2.putText(img, 'Adam is Awesome!', (10, height -10), font, 1, (255, 255, 255), 5, cv2.LINE_AA) # after font is the scale of the font (size)
                                                                            #color   #line thickness
    cv2.imshow('frame', img)


    # cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()