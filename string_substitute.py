#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: siwu
@software: PyCharm Community Edition
@time: 2017/7/6 16:15
"""


import re


input_string = u"王天 21siow'涵"
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~ ]+'
print re.sub(r1, '', input_string)

# 参考文档：
# 1.详解Python中re.sub（https://www.crifan.com/python_re_sub_detailed_introduction/）
# 2.用python进行数据预处理，过滤特殊符号，英文和数字。（适用于中文分词）
#   （http://blog.csdn.net/a1b2c3d4123456/article/details/47910649?locationNum=10）
