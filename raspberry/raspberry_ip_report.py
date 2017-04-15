#coding:utf-8
import os

get_ip_command = 'curl http://members.3322.org/dyndns/getip'
def reportIP():
    return os.system(get_ip_command)