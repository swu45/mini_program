#!/usr/bin/env python
# -*- coding:utf-8 -*-

“”“
此部分功能为获取公众号的__biz, uin, key（主要是key），
以将搜狗微信的临时链接转为永久链接；
key 的时效性据说是2小时
”“”
def wireshark_test():
    import os
    import re
    import subprocess
        
    os.chdir("D:\Program Files\Wireshark")
    batcmd = "tshark -i1 host mp.weixin.qq.com"    # 1是网卡序号，可在cmd中执行"tshark -D"查看，"host mp.weixin.qq.com"是过滤器内容
    p = subprocess.Popen(batcmd, stdout=subprocess.PIPE)
    while p.poll() is None:
       l = p.stdout.readline()  # This blocks until it receives a newline.
       if re.search('POST.+cookie', l):
           print l
           print 'biz: {}'.format(re.search('__biz=(.*?)&', l).group(1))
           print 'uin: {}'.format(re.search('uin=(.*?)&', l).group(1))
           print 'key: {}'.format(re.search('key=(.*?)&', l).group(1))
