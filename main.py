# -*- coding: UTF-8 -*-
import os
import os.path
import shutil
import sys
from xpinyin import Pinyin

# 递归遍历目录
def traversal_files(path, p):
    for name in os.listdir(path):
        dir = os.path.join(path, name)
        filetype = os.path.splitext(dir)[-1]
        if(filetype == ".png" or filetype == ".jpg"):
            name = name.replace("-","_")
            newdir = os.path.join(path, p.get_initials(name,"").lower())
            print(newdir)
            os.rename(dir, newdir)
        else:
            if os.path.isdir(dir):
                traversal_files(dir, p)


if __name__ == '__main__':
    path = '/Users/zoulin/Desktop/temp/'
    p = Pinyin()
    traversal_files(path, p)
    

