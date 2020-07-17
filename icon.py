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
    
    for imgName in imgs:
        move(file_name+"_files/", imgName)
    # 删除目录
    os.rmdir(file_name + "_files/")
    #删除压缩包
    os.remove(file_name)
    print('''
    ==========完成==========
    ''')
    zip_file.close()

def move(path, imgName):
    newpath = ""
    if "@2x.png" in imgName:
        # 重命名新路径
        newpath = infile + "/2.0x/" + imgName.replace("@2x", "")
    elif "@3x.png" in imgName:
        # 重命名新路径
        newpath = infile + "/3.0x/" + imgName.replace("@3x", "")
    else:
        newpath = infile + '/' + imgName
    #移动icon到目标路径
    shutil.move(path + imgName, newpath)
    
while(1):
    outpath = raw_input('icon压缩包或者解压过后的文件夹:')
    outpath = outpath.rstrip()
    if os.path.isdir(outpath):
        for parent,dirnames,filenames in os.walk(outpath):
            for val in filenames:
                print(val)
                move(parent+"/", val)
    else:
        # 删除右边空格
        un_zip(outpath) 
