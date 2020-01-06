# encding:utf-8

'''
@author: Hollow
@file: get_paga1.py
@time: 2019-11-07 16:07

'''

#问题1：获取网站的中文显示乱码
import requests
from bs4 import BeautifulSoup

# url = 'http://w3school.com.cn/'
# r = requests.get(url)
# r.encoding = 'gb2312'
# soup = BeautifulSoup(r.text, "lxml")
# xx = soup.find('div',id='d1').h2.text
# print (xx)

#问题2：非法字符抛出异常
# str1.decode('GBK')
# str1.decode('GBK','ignore')

#问题3：网页使用gzip压缩
# import requests
# url = 'http://www.sina.com.cn/'
# r = requests.get(url)
# print (r.text)

#解决方法
import requests
import chardet
url = 'http://www.sina.com.cn/'
r = requests.get(url)
after_gizip = r.content
print ('解压后字符串的编码为：',chardet.detect(after_gizip))
print(after_gizip.decode('utf-8'))

#问题4：读写文件的中文乱码

# import json
# title = '我们 love 你们'
# with open('title.json','w',encoding = 'utf-8') as f:
#     json.dump([title],f)

import json
title = '我们 love 你们'
with open('title.json','w',encoding = 'utf-8') as f:
    json.dump([title],f,ensure_ascii=False) #解决json中文显示问题