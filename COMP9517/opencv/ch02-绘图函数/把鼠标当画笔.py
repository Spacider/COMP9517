#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from typing import List
import cv2
import numpy as np

# 初始化为 False
drawing = False
# 如果 mode 为 true 绘制矩形， 按下 'm' 变成绘制曲线 mode=True
ix, iy = -1, -1

# 创造回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # 当按下左键时
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # 当左键按下并移动绘图 event 查看是否移动 flags 查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x,y), 3, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


if __name__ == '__main__':
    img = np.zeros((512, 512, 3), np.uint8)
    mode = False

    cv2.namedWindow('image', 0)
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == ord('m'):
            mode = not mode
        elif k == ord("q"):
            break

    cv2.destroyAllWindows()