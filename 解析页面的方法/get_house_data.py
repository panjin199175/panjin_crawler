# encding:utf-8

'''
@author: Hollow
@file: get_house_data.py
@time: 2019-10-30 14:49

'''

#获取安居客网上深圳二手房的数据

#网页地址：https://shenzhen.anjuke.com/sale/

import requests
from bs4 import BeautifulSoup
import csv

def house_detail():
    for i in range(0,10):
        print('获取第{}页房子数据'.format(str(i+1)))
        link = 'https://shenzhen.anjuke.com/sale/p{}/'.format(i)
        global headers #设置全局变量
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        html= requests.get(url=link,headers=headers)
        soup = BeautifulSoup(html.text,"lxml") #解析整个网站的页面，获取到整个HTML

        house_list = soup.find_all('li',class_='list-item') #获取所有房子的数据,是一个列表
        for houses in house_list:
            house_name = houses.find('div',class_='house-title').a.text.strip()
            price = houses.find('span',class_='price-det').text.strip()
            average_price = houses.find('span',class_='unit-price').text.strip()
            bed_room = houses.find('div',class_='details-item').span.text.strip()
            area = houses.find('div',class_='details-item').contents[3].text.strip()
            floors = houses.find('div',class_='details-item').contents[5].text.strip()
            built_year = houses.find('div',class_='details-item').contents[7].text.strip()
            house_agent = houses.find('span',class_='broker-name').text.strip()
            address = houses.find('span',class_='comm-address').text.strip().replace(' ',"").replace(r'\xa0\xa0\n'," ")
            tag_list = houses.find_all('span',class_='item-tags')
            house_tag = [i.text for i in tag_list] #列表推导式
            house_data = '房屋名称：{},' \
                         '价格：{},' \
                         '均价：{},' \
                         '几室几厅：{},' \
                         '面积：{},' \
                         '层数：{},' \
                         '建造年份：{},' \
                         '中介人：{},' \
                         '地址：{},' \
                         '标签：{}\n'.format(house_name,price,average_price,bed_room,area,floors,built_year,house_agent,address,house_tag)
            print(house_data)
            write_data(house_data)

#写入数据
def write_data(data):
    # with open(r'D:\PycharmProjects\panjin_crawler\解析页面的方法\data.txt','a+',encoding='utf-8') as f:
    #     f.write(data)
    #把数据写入CSV文件
    with open(r'D:\PycharmProjects\panjin_crawler\解析页面的方法\data.csv','a+',encoding='utf-8',newline="") as f:
        w = csv.writer(f)
        w.writerow(data)


#读取数据
def read_data():
    # with open(r'D:\PycharmProjects\panjin_crawler\解析页面的方法\data.txt','r',encoding='utf-8') as f:
    #     result = f.read().splitlines()
    #     print(result)

    #读取csv文件的数据
    with open(r'D:\PycharmProjects\panjin_crawler\解析页面的方法\data.txt','r',encoding='utf-8') as f:
        csv_readr = csv.reader(f)
        for row in csv_readr:
            print(row)

if __name__ == "__main__":
    # house_detail()
    read_data()