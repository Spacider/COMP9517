#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../pic/messi5.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# 彩色图像使用 Opencv 加载时是 BGR模式
# 但是 Matplotlib 是 RGB
# 所以彩色图像已经被Opencv 读取
# 在 Matplotlib 不会被正确显示

plt.xticks([]), plt.yticks([])
plt.show()
