# coding:utf-8
import sys
from matplotlib import pyplot as plt
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')

import cv2

def blankcallback(position):
    print '滚动条当前位置为%d'%position

# 当鼠标按下时设置 要进行绘画
drawing = False

# 如果mode为True时就画矩形，按下‘m'变为绘制曲线
mode = 0
# globalx, globaly = -1,-1
# 创建回调函数，用于设置滚动条的位置
def drawcircle(event,x,y,flags,param):
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos('s','image')
    color = (b,g,r)
    print mode
    global globalx,globaly,drawing,mode,lastx,lasty
    # 当按下左键时，返回起始的位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        globaly,globaly = x,y
        lastx = x
        lasty = y
        if mode == 2:
            b,g,r = img[y][x]
            cv2.setTrackbarPos('R','image',r)
            cv2.setTrackbarPos('G','image',g)
            cv2.setTrackbarPos('B','image',b)
            
    # 当鼠标左键按下并移动则是绘画圆形，event可以查看移动，flag查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
                
                # cv2.line(img, (`lastx,lasty), (x,y), color,s)
            if mode == 1:
                # 绘制圆圈，小圆点连接在一起成为线，1代表了比划的粗细
                cv2.circle(img,(x,y),s,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
            if mode == 4:
                print x,y
                cv2.line(img, (lastx,lasty), (x,y), color,s)
            elif mode == 3:
                cv2.rectangle(img,(lastx,lasty),(x,y),color,s)
            elif mode == 5:
                cv2.ellipse(img,((lastx+x)/2,(lasty+y)/2),(abs(lastx-x)/2,abs(lasty-y)/2),0,0,360,color,s)
            drawing = False

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     drawing = True
    #     print((x, y))
    # if event == cv2.EVENT_MOUSEMOVE:
    #     if drawing == True:
    #         # img[x,y,:-1] = [0,0,255]
    #         img[y:y+10,x:x+10] = [0,0,255]
    # if event == cv2.EVENT_LBUTTONUP:
    #     drawing = False

img = cv2.imread('images/ow.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','image',0,255,blankcallback)
cv2.createTrackbar('G','image',0,255,blankcallback)
cv2.createTrackbar('B','image',0,255,blankcallback)
cv2.createTrackbar('s','image',0,20,blankcallback)
cv2.setMouseCallback('image',drawcircle)

while True:
    #pre_img = np.zeros((100,100,3), np.uint8)
    #cv2.imshow('image',img1)
    #vtitch = np.vstack((img1, pre_img))
    cv2.imshow("image",img) 
    key = cv2.waitKey(10)&0xFFF
    if key == ord('d'):
        mode = 1
    elif key == ord('g'):
        mode = 2
    elif key == ord('r'):
        mode = 3
    elif key == ord('l'):
        mode = 4
    elif key == ord('y'):
        mode = 5
    # elif key == ord('space'):
    #     imshow()
    elif key == 27:
        break
cv2.destroyAllWindows()