import cv2
import random

img = cv2.imread('assets/Logo.png', -1)

#print(img)
#print(type(img))
#print(img.shape)
#print(img[0])
#print(img[257][45:400])
#print(img[257][400])

############################################################################################

#(301, 1320, 3)
# h    w    c
#1 height  
# 2 width/columns 
# 3 channels or color space of our image - how many values are representing each pixel (bgr)
#blue, green, red (0 means none, 255 mean all)

img = cv2.imread('assets/Logo.png', -1)

# 3 changing pixel colors
#for i in range(100):
    #for j in range(img.shape[1]):
        #img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 2 cv2.imshow('Image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

##################################################################################################

img = cv2.imread('assets/Logo.png', -1)

#copy part of the image

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
