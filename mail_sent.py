#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: siwu
@software: PyCharm Community Edition
@time: 2017/7/10 14:09
"""


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_address = raw_input('From: ')
password = raw_input('Password: ')
# 输入收件人地址:
to_address = raw_input('To: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, sent by python...', 'plain', 'utf-8')    # 参数1邮件正文, 2MIME的subtype, 3编码
msg['From'] = _format_addr('我是发件人四五 <%s>') % from_address
msg['To'] = _format_addr('你是收件人四五 <%s>') % to_address
msg['Subject'] = Header('从Python而来', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_address, password)
server.sendmail(from_address, [to_address], msg.as_string())
server.quit()