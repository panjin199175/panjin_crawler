# encding:utf-8

'''
@author: Hollow
@file: login.py
@time: 2019-11-07 17:55

'''

#处理cookie，记住你的登录信息

import requests
import json
import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')

post_url = 'http://www.santostang.com/wp-login.php'
agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
headers = {
        "Host": "www.santostang.com/",
        "Origin":"http://www.santostang.com",
        "Referer":"http://www.santostang.com/wp-login.php",
        'User-Agent': agent
    }
postdata = {
        "log":"test",
        "pwd":"a12345",
        "rememberme":"forever",
        "redirect_to":"http://www.santostang.com/wp-admin/",
        "testcookie":1
    }


login_page = session.post(post_url, data=postdata, headers=headers)
print(login_page.status_code,login_page.text)
session.cookies.save()