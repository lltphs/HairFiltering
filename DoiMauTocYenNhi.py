import cv2 as cv
import numpy as np
from copy import copy
img=cv.imread('YenNhi.jpg')
preprocessed_img=copy(img)
masked_img=np.zeros_like(img)
color_template_img=np.array([[[max(min(255,-0.4*x+0.8*y+60),0),0,min(max(0,255+0.4*x-0.8*y-60),255)] for y in range(np.shape(img)[1])] for x in range(np.shape(img)[0])]).astype(np.uint8)
state='show_color'

def paint(event,y,x,flag,params):
    global preprocessed_img,state,color_template_img
    if event!=cv.EVENT_LBUTTONDOWN:
        return
    if state=='show_color':
        print(preprocessed_img[x,y])
    elif state=='preprocessing':
        preprocessed_img[x,y]=np.array([255,255,255])
        cv.imshow('Yen Nhi',preprocessed_img)
    elif state=='change_color':
        cv.imwrite('prep_img.jpg',preprocessed_img)
        queue=[(x,y)]
        root_color=preprocessed_img[x,y]
        while len(queue)>0:
            new_point=queue.pop()
            masked_img[new_point[0],new_point[1]]=color_template_img[new_point[0],new_point[1]]
            for direction in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,-1)]:
                if np.all(np.abs(preprocessed_img[new_point[0]+direction[0],new_point[1]+direction[1]].astype(np.int16)-root_color.astype(np.int16))<50) and np.all(masked_img[new_point[0]+direction[0],new_point[1]+direction[1]]==0):
                    queue.append((new_point[0]+direction[0],new_point[1]+direction[1]))
        cv.imshow('Yen Nhi',masked_img)
        cv.imwrite('mask.jpg',masked_img)

cv.namedWindow('Yen Nhi',cv.WINDOW_NORMAL)
cv.setMouseCallback('Yen Nhi',paint)
cv.imshow('Yen Nhi',preprocessed_img)
k=cv.waitKey(0)
while k!=ord('s'):
    if k==ord('p'):
        state='preprocessing'
    elif k==ord('c'):
        state='change_color'
    k=cv.waitKey(0)