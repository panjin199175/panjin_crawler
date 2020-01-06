# encding:utf-8

'''
@author: Hollow
@file: push_redis.py
@time: 2019-11-08 17:31

'''
import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
from redis import Redis


ua = UserAgent()

headers = {'User-Agent': ua.random,
           }
def push_redis_list():
    r = Redis(host='192.168.98.103', port=6379 ,password='redisredis')
    print (r.keys('*'))

    link_list = []
    with open(r'D:\PycharmProjects\panjin_crawler\提升爬虫速度三种方法\alexca.txt', 'r') as file:
        file_list = file.readlines()
        for eachone in file_list:
            link = eachone.split('\t')[0]
            link = link.replace('\n','')
            link_list.append(link)
            if len(link_list) == 100:
                break

    for url in link_list:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'lxml')
        img_list = soup.find_all('img')
        for img in img_list:
            img_url = img['src']
            if img_url != '':
                print ("加入的图片url: ", img_url)
                r.lpush('img_url',img_url)
        print ('现在图片链接的个数为', r.llen('img_url'))
    return

push_redis_list()