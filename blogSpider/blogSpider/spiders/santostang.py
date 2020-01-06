# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from blogSpider.items import BlogspiderItem

class SantostangSpider(scrapy.Spider):
    name = 'santostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        #存放文章信息列表
        items = []
        soup = BeautifulSoup(response.text,"lxml") #解析整个网站的页面，获取到整个HTML
        frist_title = soup.find('h1',class_='post-title').a.text.strip() #获取文章第一个个标题
        # print('第一个标题是：%s' % (frist_title))
        all_title = soup.find_all('h1',class_='post-title') #获取文章所有标题
        for i in range(len(all_title)):
            #将数据封装到BlogspiderItem对象，字典类型数据
            item = BlogspiderItem()
            title = all_title[i].a.text.strip()
            link = all_title[i].a['href']

            #变成字典
            item["title"] = title
            item["link"] = link
            #根据文章的链接，发送request请求，并传递item参数
            yield scrapy.Request(url=link,meta={"item":item},callback= self.parse2)


    def parse2(self,response):
        #接收传递的item
        item = response.meta["item"]
        #解析提取文章的内容
        soup = BeautifulSoup(response.text,"lxml")
        content = soup.find('div',class_= 'view-content').text.strip().replace("\n"," ")
        item["content"] = content
        #放回item，交给item pipelines
        yield item


