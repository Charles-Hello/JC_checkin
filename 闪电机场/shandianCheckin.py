# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/17 14:40
@Auth ： maomao
@File ：shandianCheckin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
import requests

'''login登陆获取cookie'''
'''ip和key和时间戳会变化'''

import time

data_time = int(time.time())
print(data_time)

url = 'https://freemycloud.net/auth/login'
headers_str = {
    'authority': 'freemycloud.net',
    'method': 'POST',
    'path': '/auth/login',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://freemycloud.net',
    'referer': 'https://freemycloud.net/auth/login',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
}

playdata = {
    'email': '1140601003@qq.com',
    'passwd': 'aa123456',
}

respond = requests.post(url=url, data=playdata, headers=headers_str, verify=False)
a = respond.cookies
cookies_dict = requests.utils.dict_from_cookiejar(a)
# 使用utils.dict_from_cookiejar 将cookies数据类型转化为字典
a = cookies_dict

email = a['email']
expire_in = a['expire_in']
ip = a['ip']
key = a['key']
uid = a['uid']

cookies = {
    'uid': uid,
    'email': email,
    'key': key,
    'ip': ip,
    'expire_in': expire_in,
}
url = 'https://freemycloud.net/user/checkin'
headers = {
    'Host': 'freemycloud.net',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://freemycloud.net',
}
respone = requests.post(url=url, headers=headers, cookies=cookies, verify=False)
data = json.loads(respone.text)
print(data)
