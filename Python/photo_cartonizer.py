# pip install opencv-python

import cv2

img = cv2.imread('img.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayimg  = cv2.medianBlur(grayimg, 5)

edges = cv2.Laplacian(grayimg , cv2.CV_8U, ksize=5)
r,mask =cv2.threshold(edges,100,255,cv2.THRESH_BINARY_INV)

img2 = cv2.bitwise_and(img, img, mask=mask)
img2 = cv2.medianBlur(img2, 5)

cv2.imwrite("cartooned.jpg", mask)