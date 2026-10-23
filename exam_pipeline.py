import cv2
img=cv2.imread('test.png')
img_blur=cv2.GaussianBlur(img,(5,5),0)
img_hsv=cv2.cvtColor(img_blur,cv2.COLOR_BGR2HSV)
low_range=(30,50,50)
high_range=(100,255,255)
mask=cv2.inRange(img_hsv,low_range,high_range)
contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
result_img=img_blur.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow('RESULT',result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



