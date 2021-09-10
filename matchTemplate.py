import numpy as np 
import cv2

# img = cv2.imread('assets/soccer_practice.jpg', 0)
# template = cv2.imread('assets/ball.png', 0)
# h, w = template.shape

#methods for template matching

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# for method in methods:
#     img2 = img.copy()

    # result = cv2.matchTemplate(img2, template, method) #convulusion - take our template img and sliding it around our base img & seeing how close of a match it is in every single region of our base img (returns an array that shows how accurate we are in each region of our img)
    #displaying matches
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #returns min and max value and location in the array 
    # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #     location = min_loc
    # else:
    #     location = max_loc 

    # bottom_right = (location[0] + w, location[1] + h)
    # cv2.rectangle(img2, location, bottom_right, 255, 5)
    # cv2.imshow('Match', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

##################################################################################

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/shoe.png', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape

#methods for template matching

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method) 
    #displaying matches
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #returns min and max value and location in the array 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:   
        location = min_loc
    else:
        location = max_loc 

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()