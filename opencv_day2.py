import cv2

img = cv2.imread('test.png')
# 提示：test.png 的形状是 (606, 547, 3)，高=606，宽=547

# 1. 裁下上半部分（行索引 0 到 300，列全要）
top_half = img[0:300, :]

# 2. 裁下右下角的一块（你可以自己算一下具体的数值范围）
# 假设我们裁取 y=300到500，x=200到400 的区域
roi = img[300:500, 200:400]

cv2.imshow('Top Half', top_half)
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 强制缩放到固定尺寸 宽=300，高=200（注意，OpenCV 的 resize 是先宽后高！）
resized = cv2.resize(img, (300, 200))

# 4. 按比例缩放（比如长宽都缩放到原来的 0.5 倍）
h, w = img.shape[:2] # 获取原图的高和宽
half_size = cv2.resize(img, (int(w*0.5), int(h*0.5)))

cv2.imshow('Resized 300x200', resized)
cv2.imshow('Half Size', half_size)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. 在图上画一个矩形框
# 参数：图像, 左上角坐标(x,y), 右下角坐标(x,y), 颜色(B,G,R), 线条粗细
img_with_box = img.copy() # 养成好习惯，在副本上画，不污染原图
cv2.rectangle(img_with_box, (100, 100), (300, 250), (0, 0, 255), 3)

# 还可以加上文字
cv2.putText(img_with_box, "Defect", (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('With Box', img_with_box)
cv2.waitKey(0)
cv2.destroyAllWindows()