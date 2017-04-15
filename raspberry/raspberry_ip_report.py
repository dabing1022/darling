#coding:utf-8

import requests

get_ip_command = 'curl http://members.3322.org/dyndns/getip'
def reportIP():
    r = requests.get('http://members.3322.org/dyndns/getip')
    if r.status_code == 200:
        return r.text
    return '0.0.0.0'
