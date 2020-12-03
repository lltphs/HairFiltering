import cv2 as cv
import numpy as np

img=cv.imread('YenNhi.jpg')
masked_img=cv.imread('mask_best.jpg')

for x in range(np.shape(img)[0]):
    for y in range(np.shape(img)[1]):
        if np.any(masked_img[x,y]>10):
            img[x,y]=masked_img[x,y]

cv.namedWindow('Yen Nhi',cv.WINDOW_NORMAL)
cv.imshow('Yen Nhi',img)
cv.imwrite('filtered.jpg',img)
k=cv.waitKey(0)