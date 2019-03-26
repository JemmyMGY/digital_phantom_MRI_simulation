import cv2
import numpy as np


def create_phantom1(height, width):
    image = np.zeros((height, width),dtype=np.uint8)
    image[height//15:height//6, width//3:width//1] = 90
    image[height//2:height//1, width//2:width//1] = 150
    image[height//3:height//1, width//6:width//3] = 255
    return image

def create_phantom2(height, width):
    image2 = np.zeros((height, width),dtype=np.uint8)
    image2[height // 4:height// 2, width // 9:width // 3] = 255
    image2[height // 2:height// 1, width // 2:width // 1] = 150
    return image2

def create_phantom3(height, width):
    image3 = np.zeros((height, width),dtype=np.uint8)
    image3[height // 4:height // 2, width // 9:width // 3] = 150
    image3[height// 2:height // 1, width // 3:width // 2] = 255
    image3[height // 13:height // 5, width // 5:width // 1] = 90
    return image3

def t1(image3):
    shepp_t1 = np.zeros((width1, height1),dtype=np.uint8)
    for i in range(width1):
        for j in range(height1):
            if image3[i][j] == 255:  ### white matter
                shepp_t1[i][j] = 680//4
            elif image3[i][j] == 150: ### gray matter
                shepp_t1[i][j] = 810//9
            elif image3[i][j] == 90:  ### fat
                shepp_t1[i][j] =  240 //2
            elif image3[i][j] == 0: ### water
                shepp_t1[i][j] = 3000//100
            else:
                shepp_t1[i][j] = 100
    return shepp_t1

def t2(image3):
    shepp_t2 = np.zeros((height1, width1),dtype=np.uint8)
    for i in range(width1):
        for j in range(height1):
            if image3[i][j] == 255:  ### white matter
                shepp_t2[i][j] = 90 // 1
            elif image3[i][j] == 150:  ### gray matter
                shepp_t2[i][j] = 100 // 5
            elif image3[i][j] == 90:  ### fat
                shepp_t2[i][j] = 85 //2
            elif image3[i][j] == 0:  ### water
                shepp_t2[i][j] = 3000 // 100
            else:
                shepp_t2[i][j] = 50
    return shepp_t2

def pd(image3):
    shepp_pd = np.zeros((width1, height1),dtype=np.uint8)
    for i in range(width1):
        for j in range(height1):
            if image3[i][j] == 255:  ### white matter
                shepp_pd[i][j] = 500//10
            elif image3[i][j] == 150: ### gray matter
                shepp_pd[i][j] = 900//5
            elif image3[i][j] == 90:  ### fat
                shepp_pd[i][j] =  240 //3
            elif image3[i][j] == 0: ### water
                shepp_pd[i][j] = 3000//100
            else:
                shepp_pd[i][j] = 30
    return shepp_pd

def t1_t2_graph (i,j):
    return t1_mat[i][j],t2_mat[i][j]

height1, width1 = 512, 512 ####### change size from here


image = create_phantom1(height1, width1)
image2 = create_phantom2(height1, width1)
image3 = create_phantom3(height1, width1)
t1_mat = t1(image3)
t2_mat= t2(image3)
pd_mat= pd(image3)

cv2.imwrite('image1.png', image)
cv2.imwrite('image2.png', image2)
cv2.imwrite('image3.png', image3)
# cv2.imwrite('image_t1.jpg', t1_mat)
# cv2.imwrite('image_t2.jpg', t2_mat)
# cv2.imwrite('image_pd.jpg', pd_mat)
