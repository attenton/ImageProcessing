# coding=utf-8
import cv2
import numpy as np



img = np.zeros((512, 512, 3), np.uint8)
img[::] = 255
cv2.namedWindow('image')

drawing = False
# 定义鼠标的回调函数
def mouse_event(event, x, y, flags, param):
    global drawing
    # 按下鼠标左键
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        print((x, y))
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # img[x,y,:-1] = [0,0,255]
            img[y:y+10,x:x+10] = [0,0,255]
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback('image', mouse_event)

while (True):
        cv2.imshow('image', img)
        # 按下ESC键退出
        if cv2.waitKey(20) == 27:
            break

cv2.destroyAllWindows()

