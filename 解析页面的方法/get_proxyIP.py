# encding:utf-8

'''
@author: Hollow
@file: get_proxyIP.py
@time: 2019-10-31 16:53

'''

#网页网址：https://oxylabs.io/locations

import re
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
import datetime

#连接MongoDB客户端
client = MongoClient('localhost',27017)
#连接数据库blog_database，如果不存在就创建一个
db = client.blog_database
#选择该数据的集合blog，不存在也会创建
collection = db.country_ip
# from selenium import webdriver
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.image",2) #限制图片的加载
# fp.set_preference("javascript.enabled",False) #限制javascript的加载
# fp.set_preference("permissions.default.stylesheet",2) #控制 css
#
#
# link = 'https://oxylabs.io/locations'
# driver = webdriver.Firefox(firefox_profile=fp,executable_path=r'E:\Python37\geckodriver.exe')
# driver.implicitly_wait(10)
# driver.get(link)
# #找出页面所有
# time.sleep(3)
# country_list = driver.find_elements_by_css_selector('ul.continent-countries-block__list')
# time.sleep(3)
#
# for each_country_list in country_list:
#     country_name_list = each_country_list.find_elements_by_css_selector('li.country-list-item')
#     time.sleep(2)
#     for item in country_name_list:
#         country_name = item.find_element_by_css_selector('a.country-list-item__link').text.strip().replace(" ","-")
#         time.sleep(2)
#         # print(country_name)
#
#         link1 = 'https://oxylabs.io/locations/{}'.format(country_name)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
#         html= requests.get(url=link1,headers=headers)
#         soup = BeautifulSoup(html.text,"lxml") #解析整个网站的页面，获取到整个HTML
#         ip_num = soup.find('h1',class_='locations-data__title').b.text
#         print('国家：{},代理数：{}'.format(country_name,ip_num))
#         time.sleep(2)

class GetProxy():

    def __init__(self,link,headers):
        self.get_country(link,headers)

    def get_country(self,link,headers):
        html= requests.get(url=link,headers=headers)
        country_list = re.findall('<a class="country-list-item__link" href="/locations/(.*?)">',html.text)
        for i in country_list[0:]:
            country_name = i
            self.get_ip(country_name)


    def get_ip(self,name):
        link1 = link +'/' + name
        html2= requests.get(url=link1,headers=headers)
        soup = BeautifulSoup(html2.text,"lxml") #解析整个网站的页面，获取到整个HTML
        ip_num = soup.find('h1',class_='locations-data__title').b.text
        print('国家：{},代理数：{}'.format(name,ip_num))
        #将数据放进post字典中，然后用insert_one加入集合collection中
        post = {
            "country":name,
            "ip_num":ip_num,
            "data":datetime.datetime.utcnow()
            }

        collection.insert_one(post)
        time.sleep(3)

if __name__ == '__main__':
    link = 'https://oxylabs.io/locations'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    GetProxy(link,headers)



