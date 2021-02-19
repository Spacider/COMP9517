# -*- coding:utf-8 -*-

import numpy as np
import cv2

# print(cv2.__version__)

# img = cv2.imread('../pic/messi5.jpg', cv2.IMREAD_COLOR)  # 读入彩色图像，默认参数
img = cv2.imread('../pic/messi5.jpg', cv2.IMREAD_GRAYSCALE)  # 读入灰度图像，默认参数
# img = cv2.imread('../pic/messi5.jpg', cv2.IMREAD_UNCHANGED)  # 读入图像的alpha 通道

# rows, cols, ch = img.shape
rows, cols = img.shape
print('行/高：', rows, '列/宽', cols)

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 可以调节窗口大小
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)  # 自动调整
# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)  # 保 持图片比例

cv2.imshow('image', img)  # 窗口会自动调整为图像大小

# 任意键退出
k = cv2.waitKey(0)  # 返回按键的 ASCII 码
if k == 27: # 27 is Esc to exit
    cv2.destroyAllWindows()
else:
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()



