# encding:utf-8

'''
@author: Hollow
@file: get_ajax_page.py
@time: 2019-10-28 17:04

'''

import requests
import json


#爬取的网址：http://www.santostang.com/2018/07/04/hello-world/
#根据真实的URL爬取该文章的评论
#https://api-zero.livere.com/v1/comments/list?callback=jQuery112405701445625844912_1572256495834&limit=10&offset=1&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1572256495840


def get_comment(link):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

    r = requests.get(url=link,headers=headers)
    #获取json的string
    json_string = r.text
    # print(json_string)
    #提取符合JSON格式的部分,从{这个开始提取，后面两个符号不提取
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    # print(json_data)
    comment_list = json_data['results']['parents']
    # print(comment_list)
    for comment in comment_list:
        message = comment['content'] #获取评论
        print(message)


if __name__ =='__main__':

    for page in range(0,4): #获取3页是评论数据
        link = 'https://api-zero.livere.com/v1/comments/list?' \
               'callback=jQuery112406965616477517873_1572252428072&' \
               'limit=10&offset={}&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&' \
               'consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1572252428074'.format(str(page))
        print(link)
        get_comment(link)

