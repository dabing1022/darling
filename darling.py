#coding=utf8

import re
import requests
import itchat
from itchat.content import *
from config import *
#from emailSender import *

#email_sender = EmailSender()

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

@itchat.msg_register([TEXT])
def tuling_reply(msg):
    print(msg)
    content = msg[MSG_TEXT]
    userName = msg[MSG_FROM_USER_NAME]
    importantPattern = re.compile('重要')
    if (importantPattern.search(content)):
        forwardMsg = msg[MSG_FROM_USER_NAME] + ":" + content
        itchat.send(content, FILE_HELPER)
    defaultReply = '接受消息: ' + content

    if (userName == DARLING):
        # reply = YIZUER + defaultReply
        reply = ""
    else:
        # reply = YIZUER + ":" + get_response(content)
        reply = ""

    return reply

@itchat.msg_register([ATTACHMENT], isGroupChat=True)
def download_files_fromGroup(msg):
    print(msg)
    msg['Text'](msg['FileName'])
    content = u'Receive File：%s' % msg['FileName']
    email_sender.send_email(content, msg['FileName'])

@itchat.msg_register([ATTACHMENT])
def download_files_fromPerson(msg):
    print(msg)
    msg['Text'](msg['FileName'])
    content = u'Recevie File：%s' % msg['FileName']
    email_sender.send_email(content, msg['FileName'])


if __name__ == '__main__':
    # login
    itchat.auto_login(enableCmdQR=2, hotReload=True)

    # welcome
    WELCOME = u''
    WELCOME += u'Welcome, I am ChildhoodAndy AI Helper. You can call me Mike.\n'
    itchat.send(WELCOME, FILE_HELPER)

    # run
    itchat.run()
