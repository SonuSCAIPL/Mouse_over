import cv2
import numpy as np
  
ref_point = []
crop = False
  
def shape_selection(event, x, y, flags, param):

    global ref_point
  
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
  
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
      
        ref_point.append((x, y))
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        print(ref_point[0], ref_point[1])
        cv2.imshow("image", image)
  
  

# load the image, clone it, and setup the mouse callback function
image = cv2.imread("img2.jpg")

cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)


cv2.waitKey(0)
cv2.destroyAllWindows() 