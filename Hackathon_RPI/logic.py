import cv2
import numpy as np

def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img, ksize=5):
    ksize = ksize if ksize % 2 == 1 else ksize + 1
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def median_blur(img, ksize=9):
    ksize = ksize if ksize % 2 == 1 else ksize + 1
    return cv2.medianBlur(img, ksize)

def sobel_edge(img):
    gray = to_grayscale(img)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.hypot(sobelx, sobely)
    sobel = np.uint8(np.clip(sobel, 0, 255))
    return sobel

def canny_edge(img, threshold1=100, threshold2=200):
    gray = to_grayscale(img)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges

def threshold_binary(img, thresh=127):
    gray = to_grayscale(img)
    _, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    return binary

def rotate(img, angle=90):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))
    return rotated

def resize(img, width_scale=0.5, height_scale=0.5):
    h, w = img.shape[:2]
    new_w = max(1, int(w * width_scale))
    new_h = max(1, int(h * height_scale))
    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

def erode(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(img, kernel, iterations=1)

def dilate(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)

def adjust_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v = np.where(v > lim, 255, v + value).astype(np.uint8)
    final_hsv = cv2.merge((h, s, v))
    img_bright = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img_bright

def adjust_contrast(img, alpha=1.5):
    img_contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
    return img_contrast

def flip(img, mode='horizontal'):
    if mode == 'horizontal':
        return cv2.flip(img, 1)
    elif mode == 'vertical':
        return cv2.flip(img, 0)
    else:
        return img
