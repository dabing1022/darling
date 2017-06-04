# coding:utf-8

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from email.encoders import encode_base64

from itchat.content import *

# config sender email address
from_addr = ''
# config sender email password
password = ''
# smtp_server = 'smtp.126.com'
# 腾讯企业邮箱SMTP SERVER
# smtp_server = 'smtp.exmail.qq.com'
smtp_server = 'smtp.qq.com'
# to_addr = ['804928112@qq.com', '634324293@qq.com']
# config receiver email address
to_addr = ['']

class EmailSender(object):
    def __init__(self):
        self.server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
        self.server.set_debuglevel(1)
        self.server.login(from_addr, password)
        # self.server.quit()

    def send_email(self, msg, attachment = None):
        content = '<html><body><h1>微信文件转发</h1>' + '<p>%s</p>' % msg + '</body></html>'

        msg = MIMEMultipart()
        msg['From'] = u'衣卒尔 <%s>' % from_addr
        msg['To'] = u'宝 <%s>' % to_addr
        msg['Subject'] = Header(u'微信文件转发', 'utf-8').encode()
        textAtt = MIMEText(content, 'html', 'utf-8')
        msg.attach(textAtt)

        if attachment is not None:
            filename = u'' + attachment
            # 构造MIMEBase对象做为文件附件内容并附加到根容器
            contype = 'application/octet-stream'
            maintype, subtype = contype.split('/', 1)

            ## 读入文件内容并格式化
            data = open(filename, 'rb')
            fileAtt = MIMEBase(maintype, subtype)
            fileAtt.set_payload(data.read( ))
            data.close( )
            encode_base64(fileAtt)

            ## 设置附件头
            basename = os.path.basename(filename)
            fileAtt.add_header('Content-Disposition', 'attachment', filename = filename)
            msg.attach(fileAtt)

        self.server.sendmail(from_addr, to_addr, msg.as_string())


# for test
# mail = EmailSender()
# mail.send_email('test')
