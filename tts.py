# coding:utf-8

import requests
import urllib

api_key = 's2IG3y4DsQerQLs1IEELI7Xd'
secret_key = 'bb592a6ae6aa1a6086e6b8baca5da67b'
mp3_save_path = 'test.mp3'

token_url = 'https://openapi.baidu.com/oauth/2.0/token'
tts_url = 'http://tsn.baidu.com/text2audio'

token_request = requests.post(token_url, data = {'grant_type':'client_credentials', 'client_id':api_key, 'client_secret':secret_key})
if (token_request.status_code == requests.codes.ok):
    jsonResp = token_request.json()
    access_token = jsonResp['access_token']
    print(jsonResp)
    print(jsonResp['session_secret'])

    test_text = u'宝宝，你是大笨蛋。北京天气今天不错哦。'
    test_text_url_encode = urllib.request.pathname2url(test_text)
    tts_request = requests.post(tts_url, data = {'tex':test_text_url_encode, 'lan':'zh', 'tok':access_token, 'ctp':'1', 'cuid':'23242342342'})
    print(tts_request.headers['Content-Type'])
    with open(mp3_save_path, 'wb') as fd:
        fd.write(tts_request.content)

    print("播放音乐")
