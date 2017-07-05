import numpy as np
import cv2
import math
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
    h = int(img.shape[0] * percentage[0])
    w = int(img.shape[1] * percentage[1])
    return imresize(img, (h, w))

def rotate(img, angle):
    w, h, _ = img.shape
    radian = np.deg2rad(angle)
    nw = abs(np.sin(radian) * h) + abs(np.cos(radian) * w)
    nh = abs(np.cos(radian) * h) + abs(np.sin(radian) * w)
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, 1.0)
    rot_mov = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5, 0]))
    rot_mat[0,2] += rot_mov[0]
    rot_mat[1,2] += rot_mov[1]
    return cv2.warpAffine(img, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)


