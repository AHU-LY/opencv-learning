import cv2

img = cv2.imread('test.png')

# 1. 把 BGR 转成 HSV,h:色相（0-180），s:饱和度，v:亮度（0：黑色，255：亮白）
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. 打印看看它的形状（还是三维的，因为 H、S、V 算三个通道）
print("HSV形状:", hsv_img.shape)
# 我们随便取绿色气泡上的一个点，比如 y=130, x=300 附近的像素，打印它的 HSV 值
print("气泡处的 HSV 值:", hsv_img[130, 300])

cv2.imshow('Original', img)
cv2.imshow('HSV', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 定义一个颜色的范围（这里以提取黄色/绿色为例）
# 参数：图像, 颜色下限, 颜色上限
# 第一个通道 H 的范围大概是 30 到 100（涵盖黄绿）
lower_bound = (30, 50, 50) 
upper_bound = (100, 255, 255)

# 4. 生成黑白掩膜（在白名单里的变成白色，其余变黑）
mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

cv2.imshow('Mask Result', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. 找白块的轮廓（cv2.RETR_EXTERNAL 表示只找最外层，cv2.CHAIN_APPROX_SIMPLE 压缩边界）
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. 复制原图用来画框
result_img = img.copy()

# 7. 遍历找出来的每一个轮廓
for cnt in contours:
    # 计算包围轮廓的最小矩形框 (x, y, w, h)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Detected', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()