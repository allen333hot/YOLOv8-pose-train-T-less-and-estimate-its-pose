# 这个代码的功能是将文件夹下的图片每个72张复制提取出来放置到另外一个新的而文件夹下

import os
import shutil

# 指定图片文件夹路径
image_folder = r'G:\T-less\t-less_v2_train_kinect_14\14\rgb'

# 列出文件夹内所有图片文件
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# 第一张图片的索引
start_index = 11

# 指定间隔
interval = 72

# 每隔指定间隔提取图片
for i, image_file in enumerate(image_files):
    if (i - start_index) % interval == 0:
        source_path = os.path.join(image_folder, image_file)
        target_path = f'D:/Computer_Version/for_paper/ultralytics-main-v1/datasets/T-less14-increased-3th/{image_file}'
        shutil.copyfile(source_path, target_path)
