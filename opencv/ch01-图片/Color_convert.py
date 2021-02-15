#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'


import cv2

img = cv2.imread('../pic/messi5.jpg', 0)

gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gary_image", gary)
tmp = cv2.cvtColor(gary, cv2.COLOR_GRAY2BGR) # 灰度转RGB
cv2.imshow("tmp", tmp)

# 任意键退出
k = cv2.waitKey(0)  # 返回按键的 ASCII 码
if k == 27: # 27 is Esc to exit
    cv2.destroyAllWindows()
else:
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()