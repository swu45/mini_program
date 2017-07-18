#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@software: PyCharm Community Edition
"""


import zipfile
# 解压.zip文件

# f = zipfile.ZipFile(u'E:/Entrobus/report/Automation/img_download/叶广强申请表.zip', 'r')
# for file in f.namelist():
#     f.extract(file, "temp/")
“”“
源码来源：http://www.cnblogs.com/flyhigh1860/p/3884842.html
”“”


“-------------------------------我是分隔线---------------------------------”
from unrar import rarfile
“”“
注：Python下的unrar依赖RAR官方的库，
Win：
1. 先到RARLab官方下载库文件，http://www.rarlab.com/rar/UnRARDLL.exe ，然后安装；
2. 安装最好选择默认路径，一般在 C:\Program Files (x86)\UnrarDLL\ 目录下；
3. 然后重要的一步，就是添加环境变量，在系统变量（注意不是用户变量）中新建，变量名输入 UNRAR_LIB_PATH ；变量值要特别注意：
   如果你是64位系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，
   如果是32位系统就输入 C:\Program Files (x86)\UnrarDLL\UnRAR.dll ，这个从unrar安装目录的内容也能看出来它是区分64和32位的。
4. 确定保存环境变量后，重启你的PyCharm，代码不变，再运行就不会出错了。这个时候依赖库已经添加到系统环境中。
来源：http://blog.csdn.net/ysy950803/article/details/52939708
”“”
# 解压.rar文件

# file = rarfile.RarFile(u'E:/Entrobus/report/Automation/img_download/Desktop.rar')
# file.extractall(u'E:/Entrobus/report/Automation/img_download/temp/')

“”“
源码来源：http://blog.csdn.net/big_talent/article/details/52367184
”“”
