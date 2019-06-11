# 批量修改子文件夹下的图片命名格式

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


outer_path = os.path.dirname(os.path.abspath(__file__))
folder_list = os.listdir(outer_path)
# print(outer_path)
folder_list.remove("pic.py")
# print(folder_list)
for folder in folder_list:
    inner_path = os.path.join(outer_path, folder)
    file_list = os.listdir(inner_path)
    i = 1
    for item in file_list:
        total_mun_pic = len(file_list)
        if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(inner_path), item)
            dst = os.path.join(os.path.abspath(inner_path), str(folder) + '__' + str(i) + '我是修改过后的' + '.jpg')
            try:
                os.rename(src, dst)
                print(f"原始名称为: {src}, 修改后为: {dst}")
                i += 1
            except:
                continue