# 这段代码的功能：将图片文件夹中的部分随机图片剪切到另外一个文件夹中；分割训练集和测试集

import os
import random
import shutil

# 源文件夹和目标文件夹
source_folder = r'D:\Computer_Version\for_paper\ultralytics-main-v1\datasets\T-less14-increased-3th\txt'
target_folder = r'D:\Computer_Version\for_paper\ultralytics-main-v1\datasets\T-less-14-picked-for-train\labels\train'

# 获取源文件夹中所有图片的文件名
# image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.txt')]
# 随机挑选8张图片
selected_images = random.sample(image_files, 62)
# print("")

# 创建目标文件夹
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 将选中的图片剪切到目标文件夹
for image in selected_images:
    shutil.copy(os.path.join(source_folder, image), os.path.join(target_folder, image))
