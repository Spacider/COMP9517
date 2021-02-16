#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from typing import List
import cv2
import numpy as np
from matplotlib import pyplot as plt

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

'''
创立边界
'''
BLUE = [255, 255 , 0]
replicate = cv2.copyMakeBorder(img, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_REPLICATE)

reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)

constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)  # value 边界颜色

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()


