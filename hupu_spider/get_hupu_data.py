# encding:utf-8

'''
@author: Hollow
@file: get_hupu_data.py
@time: 2019-10-31 16:23

'''

#网页地址：https://bbs.hupu.com/bxj
'''
获取虎扑步行街论坛上所有帖子的数据，内容包括帖子名称、帖子链接、
作者、作者链接、创建时间、回复数、浏览数、最后回复用户和最后回复时间
'''

import requests
from bs4 import BeautifulSoup
import time
import datetime
import random
import threading
from fake_useragent import UserAgent
from hupu_spider import operation_mogondb


def get_page(link):
    ua = UserAgent()
    headers = {'User-Agent': ua.random,
                "cookie": "acw_tc=76b20f6a15725100903982350e6d954ba812a3da2e2722bbbb7aea7d51cbeb; _dacevid3=60eb3a37.3555.6d61.752f.9bdb59d01485; __gads=ID=b3ce1aacd20baaaa:T=1572510093:S=ALNI_MaoKhafSXG-BBt1P0IwgTYmLWS9gQ; _cnzz_CV30020080=buzi_cookie%7C60eb3a37.3555.6d61.752f.9bdb59d01485%7C-1; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1572510092,1572580533; PHPSESSID=18cbedb7f4b859f123eccb6294d47bf7; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e25d1f27d175-01c4fa2c23b0e5-54123310-1049088-16e25d1f29a12a%22%2C%22%24device_id%22%3A%2216e25d1f27d175-01c4fa2c23b0e5-54123310-1049088-16e25d1f29a12a%22%2C%22props%22%3A%7B%7D%7D; shihuo_target_common_go_go=1; _HUPUSSOID=d20e91b8-1c6e-4e8c-9e29-683555a8f162; _fmdata=MetXe%2FVmrWtEOj5VXn5n%2Bfe3HsmRDWSccCsfLIfNinX2%2FEw9JP1T5Cq7L%2Bufh9NhTfClIjmXyPCuxBL2vfjg9zw%2FxxDpzx9AY2559U4YisY%3D; _CLT=b0c2a05996d8b48b354e1fa4ddfc1fef; u=57084096|6JmO5omRSlIxNjY5MTE3Mzk4|ca6e|590fdcb3126ab644a299593b5987ce71|126ab644a299593b|aHVwdV80Mzk5OWVhYmUzYjVjYmUx; us=e7a09299f1f339d13c42c293cc6f36938bcb879f0f2518177270f6866663ed5c959abfbdbeab243de01540731a14b9beac136ab0c9056624321eeb138cc5c0a3; ua=16212332; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1572596275; __dacevst=e91e4d59.a13da8a5|1572598097529"
    }
    proxies = {'http':'http://106.110.212.175:9999'} #添加代理
    r = requests.get(link,headers=headers,proxies=proxies)
    soup = BeautifulSoup(r.text,"lxml")
    return soup

def get_data(data):
    post_list = []
    for data_list in data:
        post_name = data_list.find('div',class_="titlelink box").a.text.strip()
        post_link = 'https://bbs.hupu.com' + data_list.find('div',class_="titlelink box").a['href'].strip()
        author = data_list.find('div',class_="author box").a.text.strip()
        author_link = data_list.find('div',class_="author box").a['href'].strip()
        created_data = data_list.find('div',class_="author box").contents[5].text.strip()
        reply_num = data_list.find('span',class_="ansour box").text.split(" / ")[0]
        views = data_list.find('span',class_="ansour box").text.split(" / ")[1]
        end_reply_author = data_list.find('div',class_="endreply box").span.text.strip()
        end_reply_date = data_list.find('div',class_="endreply box").a.text.strip()
        if ":" in end_reply_date: #时间是这种格式的：11:03
            date_time = str(datetime.date.today()) + " " + end_reply_date
            date_time = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M")  #统一时间格式

        elif end_reply_date.find('-') == 4: #时间是这种格式的：2018-10-02
            date_time = datetime.datetime.strptime(end_reply_date,"%Y-%m-%d %H:%M").date()

        else:#时间是这种格式的:10-02
            date_time = datetime.datetime.strptime("2019-" + end_reply_date,"%Y-%m-%d").date()
        post_list.append([post_name,post_link,author,author_link,created_data,reply_num,views,end_reply_author,date_time])
    return post_list


    #     print("帖子名称：{},帖子链接：{},作者：{},作者链接：{},创建时间：{},回复数量：{},浏览数：{},最后回复人：{},最后回复时间：{}".
    #               format(post_name,post_link,author,author_link,created_data,reply_num,views,end_reply_author,date_time))
    # time.sleep(3)


if __name__ == '__main__':
    scrap_times = 0
    hupu_post = operation_mogondb.MongoAPI('localhost',27017,'hupu','post')
    for i in range(1,100):
        link = 'https://bbs.hupu.com/bxj' +'-' + str(i)
        soup = get_page(link)
        data_all= soup.find('ul',class_="for-list")
        data = data_all.find_all('li')
        post_list = get_data(data)
        for each in post_list:
            '''添加新数据'''
            # hupu_post.add({
            #     "post_name":each[0],
            #     "post_link":each[1],
            #     "author":each[2],
            #     "author_link":each[3],
            #     "created_data":str(each[4]),
            #     "reply_num":each[5],
            #     "views":each[6],
            #     "end_reply_author":each[7],
            #     "date_time":str(each[8])
            # })

            #已存在就更新
            hupu_post.update({"post_link":each[1]},{
                    "post_name":each[0],
                    "post_link":each[1],
                    "author":each[2],
                    "author_link":each[3],
                    "created_data":str(each[4]),
                    "reply_num":each[5],
                    "views":each[6],
                    "end_reply_author":each[7],
                    "date_time":str(each[8])
                })

        # time.sleep(3)
        print('获取第%d页数据完成' % (i))
        scrap_times += 1
        if scrap_times % 5 == 0:
                sleep_time = 10 + random.random()
        else:
            sleep_time = random.randint(0,2) + random.random()
        time.sleep(sleep_time)
        print ('开始休息: ', sleep_time, '秒')