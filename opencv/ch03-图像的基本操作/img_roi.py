#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from typing import List
import cv2
import numpy as np

img = cv2.imread('../pic/messi5.jpg')


'''
图像转移： 将某一块拼接
'''
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball # 直接把球取出并将另一块区域设为球， 就会出现俩球

#
# cv2.namedWindow("messi", 0)
# cv2.imshow("messi", img)
# cv2.waitKey(0)

'''
获取像素点
'''
px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

# 获取像素点更好方法
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
