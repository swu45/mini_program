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
