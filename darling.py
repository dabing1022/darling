#coding=utf8
import requests
import itchat
import re
from raspberry import raspberry_status_report
from raspberry import raspberry_ip_report

DARLING = '猪仔仔'
TULING_KEY = 'ad6c2ada8e6d4509944b7d0ab289339c'
TULING_URL = 'http://www.tuling123.com/openapi/api'
YIZUER = '衣卒尔'
FILE_HELPER = 'filehelper'
MSG_TYPE = 'Type'
MSG_TEXT = 'Text'
MSG_FROM_USER_NAME = 'FromUserName'

def get_response(msg):
    data = {
        'key'    : TULING_KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(TULING_URL, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    content = msg[MSG_TEXT]
    userName = msg[MSG_FROM_USER_NAME]
    importantPattern = re.compile('重要')
    if (importantPattern.search(content)):
        forwardMsg = msg[MSG_FROM_USER_NAME] + ":" + content
        itchat.send(content, FILE_HELPER)
    defaultReply = '接受消息: ' + content
    print(content)
    print(msg)
    print(userName)
    if (userName == DARLING):
        # reply = YIZUER + defaultReply
        reply = ""
    else:
        # reply = YIZUER + ":" + get_response(content)
        reply = ""

    return reply

itchat.auto_login(enableCmdQR=2, hotReload=True)

WELCOME = u''
WELCOME += u'欢迎使用，我是衣卒尔\n'
WELCOME += raspberry_status_report.reportStatus() + '\n'
WELCOME += u'IP:' + raspberry_ip_report.reportIP() + '\n'
itchat.send(WELCOME, FILE_HELPER)

itchat.run()
