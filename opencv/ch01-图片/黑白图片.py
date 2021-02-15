#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'


'''
创造图片
'''

import numpy as np
import cv2

size = (2560, 1600)
# 全黑， 可以用在屏保
black = np.zeros(size)
print(black[34][56])
cv2.imwrite('black.jpg', black)

# 全白
black[:]=255
print(black[34][56])
cv2.imwrite('white.jpg', black)