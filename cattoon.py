#卡通畫圖片
import cv2
import numpy as np

# 1. 读取图像
image = cv2.imread('108390.jpg')

# 2. 边缘检测
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 3. 转换为彩色卡通风格
color = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 4. 保存结果
cv2.imwrite('cartoon_output.jpg', cartoon)

cv2_imshow(cartoon)
