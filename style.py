import numpy as np
import cv2

img1 = cv2.imread( "108390.jpg", -1 )
img2 = cv2.stylization( img1 )
cv2_imshow( img1 )
cv2_imshow( img2 )
