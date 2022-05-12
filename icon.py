#!/usr/bin/python
# -*- coding: utf-8 -*-
# 解压icon包,自动转到.2x 3x文件夹中

import os
import zipfile
import shutil
from xpinyin import Pinyin

infile = input("输入flutter资源目录:")
infile = infile.rstrip()
p = Pinyin()

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
        print(imgName)
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
    newname = ""
    if "@2x.png" in imgName:
        # 重命名新路径
        newpath = infile + "/2.0x/"
        newname = imgName.replace("@2x", "")
    elif "@3x.png" in imgName:
        # 重命名新路径
        newpath = infile + "/3.0x/"
        newname = imgName.replace("@3x", "")
    else:
        newpath = infile + '/'
        newname = imgName
    #移动icon到目标路径
    newname = p.get_initials(newname.replace("-","_"),"").lower()
    respath = get_path_name(newpath, newname, 0)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.move(path + imgName, respath)

def get_path_name(path, name, index):
    print(path + name)
    if not os.path.exists(path + name):
        return path + name
    else:
        _temp = "%s.png" % index
        index += 1
        if _temp in name:
            name = name.replace(_temp, "%s.png" % index)
        else:    
            name = name.replace(".png", "%s.png" % index)
        return get_path_name(path, name, index)
    
while(1):
    outpath = input('icon压缩包或者解压过后的文件夹:')
    outpath = outpath.rstrip()
    if os.path.isdir(outpath):
        for parent,dirnames,filenames in os.walk(outpath):
            for val in filenames:
                print(val)
                move(parent+"/", val)
            # os.rmdir(parent)
    else:
        # 删除右边空格
        un_zip(outpath) 
