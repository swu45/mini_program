#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: siwu
@software: PyCharm Community Edition
@time: 2017/3/14 20:15
"""


import re
import sys


input_string = raw_input('请输入搜索词: ')
filter_list = ['翻墙', '代理', 'MD5', 'VPN']
for i_fl in filter_list:
    re_pattern = re.compile(i_fl, re.I)
    output_string = re_pattern.search(input_string)
    if output_string:
        print '输入内容包含违禁词: {}'.format(i_fl)
        sys.exit()