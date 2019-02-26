## Finding Tiny Faces
### 介绍
Finding Tiny Faces是一篇可以高效识别小人脸的论文。
文章作者主要实现了多尺度识别图片金字塔，并且识别的时候添加了背景信息和多层特征来辅助识别，最后取得了很好的效果。
### 运行
运行文件为tiny_face_eval.py，可以使用如下命令运行(mat2tf.pkl为参数文件):
```bash
python tiny_face_eval.py
  --weight_file_path /path/to/pickle_file
  --data_dir /path/to/input_image_directory
  --output_dir /path/to/output_directory
```
如有问题，可参考code/README.md

### 实验结果
![Finding Tiny Faces.jpg](Finding Tiny Faces.jpg)