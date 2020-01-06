# encding:utf-8

'''
@author: Hollow
@file: single_thread.py
@time: 2019-11-06 18:02

'''
'''单线程'''


import requests
import time

link_list = []
with open(r'D:\PycharmProjects\panjin_crawler\提升爬虫速度三种方法\alexca.txt','r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[0]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
for eachone in link_list:
    try:
        r = requests.get(eachone)
        print(r.status_code,eachone)
    except Exception as e:
        print("Error:",e)

end  = time.time()
print("串行的总时间为：",end - start)
