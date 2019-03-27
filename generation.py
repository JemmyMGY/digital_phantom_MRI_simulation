import cv2
import numpy as np
from matplotlib import pyplot as plt


def create_phantom1(height, width):
    in_image = np.zeros((height, width),dtype=np.uint8)
    in_image[height//15:height//6, width//3:width//1] = 90
    in_image[height//2:height//1, width//2:width//1] = 150
    in_image[height//3:height//1, width//6:width//3] = 255
    return in_image

def create_phantom2(height, width):
    in_image= np.zeros((height, width),dtype=np.uint8)
    in_image[height // 4:height// 2, width // 9:width // 3] = 255
    in_image[height // 2:height// 1, width // 2:width // 1] = 150
    return in_image

def create_phantom3(height, width):
    in_image = np.zeros((height, width),dtype=np.uint8)
    in_image[height // 4:height // 2, width // 9:width // 3] = 150
    in_image[height// 2:height // 1, width // 3:width // 2] = 255
    in_image[height // 13:height // 5, width // 5:width // 1] = 90
    return in_image


height1, width1 = 512,512

image1 = create_phantom1(height1, width1)
image2 = create_phantom2(height1, width1)
image3 = create_phantom3(height1, width1)

cv2.imwrite('image1.png', image1)
cv2.imwrite('image2.png', image2)
cv2.imwrite('image3.png', image3)
