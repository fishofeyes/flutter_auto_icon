#!/usr/bin/python
# -*- coding: utf-8 -*-
# 解压icon包,自动转到.2x 3x文件夹中

import os
import zipfile
import shutil
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

infile = raw_input("输入flutter资源目录:")


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    imgs = []
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
        imgs.append(names)
    
    for img_path in imgs:
        print(img_path)
        newpath = ""
        if "@2x.png" in img_path:
            # 重命名新路径
            newpath = infile + "/2.0x/" + img_path.replace("@2x", "")
        elif "@3x.png" in img_path:
            # 重命名新路径
            newpath = infile + "/3.0x/" + img_path.replace("@3x", "")
        else:
            newpath = infile + '/' + img_path
        #移动icon到目标路径
        shutil.move(file_name + "_files/" + img_path, newpath)
    # 删除目录
    os.rmdir(file_name + "_files/")
    #删除压缩包
    os.remove(file_name)
    print('''
    ==========完成==========
    ''')
    zip_file.close()
    
while(1):
    outpath = raw_input('icon压缩包:')
    # 删除右边空格
    un_zip(outpath.rstrip()) 