# encding:utf-8

'''
@author: Hollow
@file: re_.py
@time: 2019-10-29 21:36

'''
#正则提取
#详细正则表达式文档地址：https://docs.python.org/3/library/re.html

# 基本三种方法：
# re.match() 只能从字符串的起始位置进行匹配
# re.search() 扫描整个字符串并返回第一个成功的匹配
# re.findall() 可以找到所有的匹配

import requests
import re

link = 'http://www.santostang.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = requests.get(url=link,headers=headers)
html = r.text
# print(html)

#获取文章所有的title
title_list = re.findall('<h1 class="post-title"><a href=.*>(.*?)</a></h1>',html)

print(title_list)