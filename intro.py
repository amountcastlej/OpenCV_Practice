import cv2

# 1 load an image

img = cv2.imread('assets/Logo.png', -1)

#pixel values for height and width use for example: (400, 400)

#default CV2 loads images in bgr pattern 
# -1, cv2.IMREAD_COLOR

#load image in gray 
# 0, cv2.IMREAD_GRAYSCALE

#ignoring transparency 
# 1, cv2.IMREAD_UNCHANGED

#2 show an image & '' is for showing the image in a window

cv2.imshow('image', img)

#Ability to close the window

cv2.waitKey(0)  #allows you to wait an infinite amount of time (0) to press any keys on the keyboard, 5 means wait 5 seconds to press a key, else it will be skipped
cv2.destroyAllWindows()
########################################################################################################################################################################

# load an image

img = cv2.imread('assets/Logo.png', -1)

# resize
img = cv2.resize(img, (400, 400))
#change the image to a fraction of the image size or double w/ 2

#pixel values for height and width use for example: (400, 400)

#default CV2 loads images in bgr pattern 
# -1, cv2.IMREAD_COLOR

#load image in gray 
# 0, cv2.IMREAD_GRAYSCALE

#ignoring transparency 
# 1, cv2.IMREAD_UNCHANGED

# show an image & '' is for showing the image in a window

cv2.imshow('image', img)

#Ability to close the window

cv2.waitKey(0)  #allows you to wait an infinite amount of time (0) to press any keys on the keyboard, 5 means wait 5 seconds to press a key, else it will be skipped
cv2.destroyAllWindows()

#####################################################################################################################################################################
# load an image

img = cv2.imread('assets/Logo.png', -1)

# resize
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#change the image to a fraction of the image size or double w/ 2

#pixel values for height and width use for example: (400, 400)

#default CV2 loads images in bgr pattern 
# -1, cv2.IMREAD_COLOR

#load image in gray 
# 0, cv2.IMREAD_GRAYSCALE

#ignoring transparency 
# 1, cv2.IMREAD_UNCHANGED

#Ability to close the window

cv2.waitKey(0)  #allows you to wait an infinite amount of time (0) to press any keys on the keyboard, 5 means wait 5 seconds to press a key, else it will be skipped
cv2.destroyAllWindows()

#######################################################################################################################################################################

# load an image

img = cv2.imread('assets/Logo.png', -1)

# resize
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#change the image to a fraction of the image size or double w/ 2

# rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

#pixel values for height and width use for example: (400, 400)

#default CV2 loads images in bgr pattern 
# -1, cv2.IMREAD_COLOR

#load image in gray 
# 0, cv2.IMREAD_GRAYSCALE

#ignoring transparency 
# 1, cv2.IMREAD_UNCHANGED

#show an image & '' is for showing the image in a window

cv2.imshow('image', img)

#Ability to close the window

cv2.waitKey(0)  #allows you to wait an infinite amount of time (0) to press any keys on the keyboard, 5 means wait 5 seconds to press a key, else it will be skipped
cv2.destroyAllWindows()

#############################################################################################################################################################################

# load an image

img = cv2.imread('assets/Logo.png', -1)

# resize
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#change the image to a fraction of the image size or double w/ 2

# rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# save image file
cv2.imwrite('new_img.png', img)

#pixel values for height and width use for example: (400, 400)

#default CV2 loads images in bgr pattern 
# -1, cv2.IMREAD_COLOR

#load image in gray 
# 0, cv2.IMREAD_GRAYSCALE

#ignoring transparency 
# 1, cv2.IMREAD_UNCHANGED

#2 show an image & '' is for showing the image in a window

cv2.imshow('image', img)

#Ability to close the window

cv2.waitKey(0)  #allows you to wait an infinite amount of time (0) to press any keys on the keyboard, 5 means wait 5 seconds to press a key, else it will be skipped
cv2.destroyAllWindows()

##########################################################################################################################################################################################