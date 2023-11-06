import cv2
import numpy as np

# 1. 读取图像
image = cv2.imread('108390.jpg')

# 2. 调整亮度和对比度
alpha = 1.5  # 调整亮度
beta = 25  # 调整对比度
result = cv2.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), 0, beta)

# 3. 锐化图像
kernel = np.array([[-1, -1, -1],
                  [-1, 9, -1],
                  [-1, -1, -1]])
result = cv2.filter2D(result, -1, kernel)

# 4. 去噪
result = cv2.fastNlMeansDenoisingColored(result, None, 10, 10, 7, 21)

# 5. 调整颜色饱和度
hsv = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
hsv[:, :, 1] = hsv[:, :, 1] * 1.5
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 6. 保存结果
cv2.imwrite('output.jpg', result)
cv2_imshow(result)
