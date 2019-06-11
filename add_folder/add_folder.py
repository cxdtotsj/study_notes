# 批量修改子文件夹下的图片命名格式

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


outer_path = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(outer_path, "folder.txt")
# print(data_file)
with open(data_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        folder = os.path.join(os.path.abspath(outer_path), line)
        folder = folder.strip()
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"文件夹{folder}创建成功!")
        else:
            print(f"文件夹{folder}已存在!")