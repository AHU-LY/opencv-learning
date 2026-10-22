import cv2

img=cv2.imread('test.png')
h,w=img.shape[:2]
img1=img[175:220,508:547]

img2=cv2.resize(img1,(200,200))

img3=img2.copy()
cv2.rectangle(img3,(10,10),(100,50),(255,0,0),2)
cv2.putText(img3,'Liu Yang',(10,9),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv2.imshow('Tou Xiang', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('avatar_result.jpg', img3)
