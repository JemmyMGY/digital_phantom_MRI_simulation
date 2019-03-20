import cv2
import numpy as np
import sys


def create_blank(width, height):
    image = np.zeros((height, width))
    image[20:100, 10:150] = 255
    image[70:200, 200:250] = 125
    image[140:250, 50:150] = 50

    return image


def t1(image):
    shepp = np.zeros((height1, width1))
    for i in range(width1):
        for j in range(height1):
            if image[i][j] == 255:
                shepp[i][j] = 255//3
            elif image[i][j] == 125:
                shepp[i][j] = 125 * 3 // 2
            elif image[i][j] == 80:
                shepp[i][j] = 80 + 100
            elif image[i][j] == 0:
                shepp[i][j] = 50
    return shepp


width1, height1 = 512, 512

image = create_blank(width1, height1)
t1_we = t1(image)

cv2.imwrite('image1.jpg', image)
cv2.imwrite('image2.jpg', t1_we)
