# encding:utf-8

'''
@author: Hollow
@file: get_lxml.py
@time: 2019-10-30 14:29

'''

#利用lxml里的xpath 方法解析网页

import requests
from lxml import etree

link = 'http://www.santostang.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = requests.get(url=link,headers=headers)

html = etree.HTML(r.text) #解析为lxml格式
title_list = html.xpath('//h1[@class="post-title"]/a/text()')
print(title_list)