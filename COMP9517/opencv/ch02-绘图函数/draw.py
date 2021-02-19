#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

import numpy as np
import cv2

'''
    @ img: 你想绘制图形的幅图像
    @ color: 形状的颜色 以 RGB 为例， 需要传入一个元祖BGR 例如 255，0，0
    代表蓝色， 第一个是蓝色通道， 第二个绿色通道，第三个是红色通道，对于灰度图只需要传入灰度值
    @ thickness 线条的粗细，如果给一个闭合图形，置为 -1 那么这个图形就会被填充，默认值是1
    @ linetype 线条的类型 8： 链接，抗锯齿 默认为8 cv2.LiINE_AA 为抗锯齿， 线条会特别平滑
'''

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a blue line with thickness of 5 px
cv2.line(img, pt1=(0, 0), pt2=(511, 511), color=(255, 0, 0), thickness=5)
# 使用 cv2.polylines() 方法能够快速的绘制多条线

cv2.arrowedLine(img, pt1=(21, 13), pt2=(151, 401), color=(255, 0, 0), thickness=5)

# 正方形，提供对角点 颜色
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# ellipse(图片， 中心点位置坐标， 长轴和短轴长度， 椭圆沿逆时针方向旋转的角度。
# 椭圆沿顺时针方向起始的角度和结束角度 如果 0 到 360 就是整个椭圆
cv2.ellipse(img, center=(256, 256), axes=(100, 50), angle=0, startAngle=0, endAngle=180, color=255, thickness=-1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text= 'bottomLeftOrigin', org=(10, 400), fontFace=font, fontScale=1, color=(255, 255, 255), thickness=1, bottomLeftOrigin=True)
cv2.putText(img, text='OpenCV', org=(10, 500), fontFace=font, fontScale=4, color=(255, 255, 255), thickness=2)

winname = 'example'
cv2.namedWindow(winname, 0)
cv2.imshow(winname, img)
cv2.imwrite("example.png", img)