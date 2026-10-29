import cv2
import numpy as np
img=cv2.imread('test.png')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(gray_img,(5,5),0)
edge=cv2.Canny(img_blur,50,150)
kernel=np.ones((3,3),np.uint8)
dilation=cv2.dilate(edge,kernel,iterations=1)
contours, hierarchy =cv2.findContours(dilation,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result_img = img.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow('1', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()