# encding:utf-8

'''
@author: Hollow
@file: operation_mongo.py
@time: 2019-10-31 15:06

'''

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import datetime

#连接MongoDB客户端
client = MongoClient('localhost',27017)
#连接数据库blog_database，如果不存在就创建一个
db = client.blog_database
#选择该数据的集合blog，不存在也会创建
collection = db.blog

link = 'http://www.santostang.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = requests.get(url=link,headers=headers)
soup = BeautifulSoup(r.text,"lxml") #解析整个网站的页面，获取到整个HTML
frist_title = soup.find('h1',class_='post-title').a.text.strip() #获取文章第一个个标题
all_title = soup.find_all('h1',class_='post-title') #获取文章所有标题
for i in range(len(all_title)):
    title = all_title[i].a.text.strip()
    url = all_title[i].a['href']

    #将数据放进post字典中，然后用insert_one加入集合collection中
    post = {
        "url":url,
        "title":title,
        "data":datetime.datetime.utcnow()
    }

    collection.insert_one(post)