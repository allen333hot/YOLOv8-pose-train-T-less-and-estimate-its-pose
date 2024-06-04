# 这个代码的功能是从0依次变大重命名
# 此代码作用：对图片文件夹进行重命名
import os

folder_path = r'D:\Computer_Version\for_paper\ultralytics-main-v1\datasets\T-less14-increased-3th'
file = os.listdir(folder_path)

file.sort()

for i, file_name in enumerate(file):
    # print("i=", i)
    new_file_name = 'T-less14-' + str(i+99) + '.png'
    # 拼接新旧文件路径
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)
