# encding:utf-8

'''
@author: Hollow
@file: get_ocr.py
@time: 2019-11-12 14:53

'''

import requests
from bs4 import BeautifulSoup
import pytesseract
import os
from PIL import Image

#OCR处理验证码

def get_captcha():
    #获取验证码图片所在的url
    r = session.get('http://www.santostang.com/wp-login.php?action=register', headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    captcha_url = soup.find("img", id="captcha_code_img")["src"]
    # 获取验证码图片
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    # captcha = input("please input the captcha\n>")
    # return captcha

def operation_ocr():
    #把彩色图像转化成灰色
    im = Image.open('captcha.jpg')
    gray = im.convert('L')
    gray.show()
    gray.save("captcha_gray.jpg")

    #二值化处理，加深验证码颜色
    threshold = 150
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = gray.point(table, '1')
    out.show()
    out.save("captcha_thresholded.jpg")

    th = Image.open('captcha_thresholded.jpg')
    code = pytesseract.image_to_string(th)
    print(code)
    return code


def register(account, email):
    post_url = 'http://www.santostang.com/wp-login.php?action=register'
    postdata = {
        'user_login': account,
        'user_email': email,
        'redirect_to': '',
        'ux_txt_captcha_challenge_field':operation_ocr() # 调用operation_ocr函数，获取验证码数字
        }

    # 提交POST请求，进行注册
    register_page = session.post(post_url, data=postdata, headers=headers)
    # 若输出打印结果为200，则表示注册成功
    print(register_page.status_code)

if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    headers = {
        "Host": "www.santostang.com",
        "Origin":"http://www.santostang.com",
        "Referer":"http://www.santostang.com/wp-login.php",
        'User-Agent': agent
    }
    session = requests.session()
    # 调用注册函数进行注册
    account = 'ppp123' #改成自己用户名
    email = 'a12345@qq.com' # 改成自己邮箱
    get_captcha()
    register(account, email)