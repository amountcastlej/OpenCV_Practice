import numpy as np 
import cv2


img = cv2.imread('assets/pokemon.jpg')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray scale

# Corner detection                                # minimum distance between two corners (two points)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
                        #pass img, # of best corners to return, quality of corners from 0 to 1

corners = np.int0(corners) #turn float integers and turn into integers

for corner in corners:
    x, y = corner.ravel() # ravel gets rid of brackets around the interior array [[[1, 2, 3]]] => [1,2,3]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1) # draw corners of the image

# Draw lines between corners 

for i in range(len(corners)): #loop thru corners
    for j in range(i + 1, len(corners)): #loop thru all other corners we haven't already looped thru 
        corner1 = tuple(corners[i][0]) # get corner 1
        corner2 = tuple(corners[j][0]) # get corner 2           # generate three colors between 0 to 255
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)) 
        #map applies the function to each array of generating colors & returns a new array of the result from the function
        # (anonymous function) lambda generates the function, that passes x in a parameter & return value comes after : which is int(x), which is what it will return 
        
        cv2.line(img, corner1, corner2, color, 1) #draw a line between the two corners


cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
