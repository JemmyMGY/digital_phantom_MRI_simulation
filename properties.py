import cv2
import numpy as np

def t1(in_image):
    shepp_t1 = np.zeros((in_image.shape[0],in_image.shape[1]),dtype=np.uint8)
    for i in range(in_image.shape[0]):
        for j in range(in_image.shape[1]):
            if in_image[i][j] == 255:  ### white matter
                shepp_t1[i][j] = 10
            elif in_image[i][j] == 150:  ### gray matter
                shepp_t1[i][j] = 70
            elif in_image[i][j] == 90:  ### fat
                shepp_t1[i][j] = 150
            elif in_image[i][j] == 0:  ### water
                shepp_t1[i][j] = 255
            else:
                shepp_t1[i][j] = 255
    return shepp_t1


def t2(in_image):
    shepp_t2 = np.zeros((in_image.shape[0], in_image.shape[1]),dtype=np.uint8)
    for i in range(in_image.shape[0]):
        for j in range(in_image.shape[1]):
            if in_image[i][j] == 255:  ### white matter
                shepp_t2[i][j] = 50
            elif in_image[i][j] == 150:  ### gray matter
                shepp_t2[i][j] = 255
            elif in_image[i][j] == 90:  ### fat
                shepp_t2[i][j] = 10
            elif in_image[i][j] == 0:  ### water
                shepp_t2[i][j] = 200
            else:
                shepp_t2[i][j] = 200
    return shepp_t2

def pd(in_image):
    shepp_pd = np.zeros((in_image.shape[0], in_image.shape[1]),dtype=np.uint8)
    for i in range(in_image.shape[0]):
        for j in range(in_image.shape[1]):
            if in_image[i][j] == 255:  # white matter
                shepp_pd[i][j] = 50
            elif in_image[i][j] == 150:  # gray matter
                shepp_pd[i][j] = 140
            elif in_image[i][j] == 90:  # fat
                shepp_pd[i][j] = 120
            elif in_image[i][j] == 0:  # water
                shepp_pd[i][j] = 30
            else:
                shepp_pd[i][j] = 30

    return shepp_pd




# def wheelEvent(self, event):
#     increaseFactor = 10
#     decreaseFactor = -10
#
#     if event.angleDelta().y() > 0:
#         zoomFactor = increaseFactor
#         for i in range(image.shape[0]):
#             for j in range(image.shape[1]):
#                 if image[i][j] < 245:
#                     image[i][j] = image[i][j] + increaseFactor
#     else:
#         zoomFactor = decreaseFactor
#         for i in range(image.shape[0]):
#             for j in range(image.shape[1]):
#                 if image[i][j] > 10:
#                     image[i][j] = image[i][j] - decreaseFactor

