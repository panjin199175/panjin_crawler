# encding:utf-8

'''
@author: Hollow
@file: login1.py
@time: 2019-11-08 10:39

'''

import requests
import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookies 未能加载')

#检查是否登录成功
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {
        "Host": "www.javascriptc.com",
        # "Origin":"http://www.santostang.com",
        "Referer":"https://www.javascriptc.com/",
        'User-Agent': agent
    }

def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.javascriptc.com/special/bat-question"
    login_code = session.get(url, headers=headers,allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False

print(isLogin())