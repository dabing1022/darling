#coding=utf8

import re
import requests
import itchat
from itchat.content import *
from config import *
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date
#from emailSender import *

#email_sender = EmailSender()
tuling_reply_on = False

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
    global tuling_reply_on
    reply = ""
    print(msg)
    content = msg[MSG_TEXT]
    userName = msg[MSG_FROM_USER_NAME]

    print(msg[MSG_TO_USER_NAME])
    if msg[MSG_TO_USER_NAME] == FILE_HELPER:
        if re.search(r'tuling_reply_on', content):
            print("tuling on")
            tuling_reply_on = True
        elif re.search(r'tuling_reply_off', content):
            print("tuling off")
            tuling_reply_on = False

    importantPattern = re.compile('重要')
    if (importantPattern.search(content)):
        itchat.send(content, FILE_HELPER)

    if tuling_reply_on:
        reply = MIKE + ":" + get_response(content)
    else:
        pass

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

def job():
    time_report = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(time_report)
    itchat.send(time_report, FILE_HELPER)

if __name__ == '__main__':
    # login
    itchat.auto_login(enableCmdQR=2, hotReload=False)

    # welcome
    WELCOME = u''
    WELCOME += u'Welcome, I am ChildhoodAndy AI Helper. You can call me Mike.\n'
    itchat.send(WELCOME, FILE_HELPER)

    sched = BlockingScheduler()
    # sched.add_job(job, 'interval', seconds=5)
    # sched.add_job(job, 'date', run_date = datetime(2018, 1, 1, 16, 43, 0))
    # sched.start()

    # run
    itchat.run()
