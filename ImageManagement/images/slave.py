import numpy as np
import cv2 as cv
from scipy.misc import *




def gray(img):
    chan = np.dot(img, [0.299, 0.587, 0.114])
    chan = np.uint8(chan)
    return chan

def blur(img, degree=0.5):
    ksize_h = int(degree * img.shape[0])
    ksize_w = int(degree * img.shape[1])
    if ksize_h % 2 == 0:
        ksize_h += 1
    if ksize_w % 2 == 0:
        ksize_w += 1
    if ksize_h <= 1 or ksize_w <= 1:
        return img
    return cv2.GaussianBlur(img, (ksize_h, ksize_w), degree * 50)


def binaryzation(img, max_value=255, ksize=33, inv=False):
    gray_img = gray(img).astype('uint8')
    if inv:
         return cv2.adaptiveThreshold(gray_img, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                 cv2.THRESH_BINARY_INV, ksize, 0)
    return cv2.adaptiveThreshold(gray_img, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                 cv2.THRESH_BINARY, ksize, 0)


def rescale(img, percentage):
    h = img.shape[0] * percentage[0]
    w = img.shape[1] * percentage[1]
    return imresize(img, (h, w))


