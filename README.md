# ImageProcessing
2018年秋季学期的课程 数字图像处理

#### 主要有三个project
* 画图板
* 人脸识别
* 图像去模糊

##### 画图板
画图板利用的是js实现的网页画图板，用的是fabric框架，可以试想矢量画图，图像可伸缩

##### 人脸识别
人脸识别参考的论文是[finding tiny face](https://arxiv.org/pdf/1612.04402.pdf)
利用resnet101，多尺度人脸识别，文章主要是通过一些实验，来验证论文实现的代码的参数的正确性。

##### 图像去模糊
图像去模糊参考的论文是由腾讯优图和港中文联合发表的[Scale-recurrent Network for Deep Image Deblurring](http://www.xtao.website/projects/srndeblur/srndeblur_cvpr18.pdf)
论文中结合前人工作，提出了新的网络结构，一种多尺度循环网络。最后达到了the state of art的效果。
