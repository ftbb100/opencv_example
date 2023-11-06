#鉛筆素描特效
import numpy as np
import cv2

img = cv2.imread( "108390.jpg", -1 )
img1, img2 = cv2.pencilSketch( img )
cv2_imshow( img )
cv2_imshow( img1 )
cv2_imshow( img2 )
