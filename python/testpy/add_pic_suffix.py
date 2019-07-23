
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

dir_path = os.path.dirname(os.path.abspath(__file__))
dir_pic = "".join([dir_path,r"\pic"])

# 方法一
def file_name(file_dir):
    for _,_,files in os.walk(dir_pic):
        for file_name in files:
            file_pic = "".join([file_name,".jpg"])
            os.chdir(dir_pic)   # 切换至需要修改文件的目录
            os.rename(file_name,file_pic)

file_name(dir_pic)


# 方法二
files = os.listdir(dir_pic)
for filename in files:
    portion = os.path.splitext(filename)
    print(portion)
    if portion[1] == "":
        newname = portion[0]+'.jpg'
        os.chdir(dir_pic)
        os.rename(filename,newname)