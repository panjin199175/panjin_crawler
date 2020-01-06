# encding:utf-8

'''
@author: Hollow
@file: get_bs4.py
@time: 2019-10-30 10:35

'''

#利用BeautifulSoup库解析网页

from bs4 import BeautifulSoup
import requests

link = 'http://www.santostang.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = requests.get(url=link,headers=headers)
soup = BeautifulSoup(r.text,"lxml") #解析整个网站的页面，获取到整个HTML
# frist_title = soup.find('h1',class_='post-title').a.text.strip() #获取文章第一个个标题
# all_title = soup.find_all('h1',class_='post-title') #获取文章所有标题
# for i in range(len(all_title)):
#     title = all_title[i].a.text.strip()
#     print(title)

# print(soup.prettify()) #对获取到的Html进行美化

#提取对象的三种方法
#1遍历文档树
#2搜索文档树 find(),find_all()
#3CSS选择器 soup.select()

#1遍历文档树
# print(soup.header.h1) #获取<h1>标签
# print(soup.header.div.contents) #获取DIV标签的所有子节点，并以列表形式输出
# for child in soup.header.div.children:  #获取所有子标签 ，是下一级的节点
#     print(child)


#3CSS选择器
# print(soup.select('header > h1')) #遍历header标签下的H1标签