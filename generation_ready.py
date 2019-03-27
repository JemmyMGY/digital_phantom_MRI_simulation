import cv2
import numpy as np


def t1(image3):
    shepp_t1 = np.zeros((image3.shape[0], image3.shape[1]), dtype=np.uint8)
    for i in range(image3.shape[0]):
        for j in range(image3.shape[1]):
            if image3[i][j] == 255:  # white matter
                shepp_t1[i][j] = 680//4
            elif image3[i][j] == 150:  # gray matter
                shepp_t1[i][j] = 810//9
            elif image3[i][j] == 90:  # fat
                shepp_t1[i][j] = 240 // 2
            elif image3[i][j] == 0:  # water
                shepp_t1[i][j] = 3000//100
            else:
                shepp_t1[i][j] = 3000 // 100
    return shepp_t1


def t2(image3):
    shepp_t2 = np.zeros((image3.shape[0], image3.shape[1]))
    for i in range(image3.shape[0]):
        for j in range(image3.shape[1]):
            if image3[i][j] == 255:  # white matter
                shepp_t2[i][j] = 90 // 1
            elif image3[i][j] == 150:  # gray matter
                shepp_t2[i][j] = 100 // 5
            elif image3[i][j] == 90:  # fat
                shepp_t2[i][j] = 85 // 2
            elif image3[i][j] == 0:  # water
                shepp_t2[i][j] = 3000 // 100
            else:
                shepp_t2[i][j] = 3000 // 100

    return shepp_t2


def pd(image3):
    shepp_pd = np.zeros((image3.shape[0], image3.shape[1]))
    for i in range(image3.shape[0]):
        for j in range(image3.shape[1]):
            if image3[i][j] == 255:  # white matter
                shepp_pd[i][j] = 500//10
            elif image3[i][j] == 150:  # gray matter
                shepp_pd[i][j] = 900//5
            elif image3[i][j] == 90:  # fat
                shepp_pd[i][j] = 240 // 3
            elif image3[i][j] == 0:  # water
                shepp_pd[i][j] = 3000//100
            else:
                shepp_pd[i][j] = 3000 // 100

    return shepp_pd


def t1_t2_graph(i, j):
    return t1_mat[i][j], t2_mat[i][j]


def wheelEvent(self, event):
    increaseFactor = 10
    decreaseFactor = -10

    if event.angleDelta().y() > 0:
        zoomFactor = increaseFactor
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] < 245:
                    image[i][j] = image[i][j] + increaseFactor
    else:
        zoomFactor = decreaseFactor
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] > 10:
                    image[i][j] = image[i][j] - decreaseFactor
