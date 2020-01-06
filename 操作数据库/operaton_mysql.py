# encding:utf-8

'''
@author: Hollow
@file: operaton_mysql.py
@time: 2019-10-31 10:19

'''

# import pymysql

# #打开数据库连接
# db = pymysql.connect('localhost','root','123456','scraping')
# #使用cursor()方法获取操作游标
# cur = db.cursor()
#
# #sql插入表
# sql = "insert into urls(url,content) values ('https://beijin.anjuke.com/sale/','这是安居客北京的房子网址')"
#
# try:
#     #执行sql
#     cur.execute(sql)
#     #提交
#     db.commit()
# except:
#     #如果发生错误
#     db.rollback()#回滚
# db.close()#关闭数据库


from bs4 import BeautifulSoup
import requests
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','123456','scraping',charset='utf8')
#使用cursor()方法获取操作游标
cur = db.cursor()

link = 'http://www.santostang.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
r = requests.get(url=link,headers=headers)
soup = BeautifulSoup(r.text,"lxml") #解析整个网站的页面，获取到整个HTML
frist_title = soup.find('h1',class_='post-title').a.text.strip() #获取文章第一个个标题
all_title = soup.find_all('h1',class_='post-title') #获取文章所有标题
for i in range(len(all_title)):
    title = all_title[i].a.text.strip()
    url = all_title[i].a['href']
    print(url,title)
    sql = "insert into urls(url,content) values ('{}','{}')".format(url,title)
    cur.execute(sql)
db.commit()
db.close()