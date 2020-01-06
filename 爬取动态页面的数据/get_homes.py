# encding:utf-8

'''
@author: Hollow
@file: get_homes.py
@time: 2019-10-29 16:42

'''

#网页地址：https://www.airbnb.com/s/ShenZhen--China/homes

from selenium import webdriver
import time


def get_homes():
    #限制图片的加载
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.image",2) #限制图片的加载
    fp.set_preference("javascript.enabled",False) #限制javascript的加载
    fp.set_preference("permissions.default.stylesheet",2) #控制 css
    driver = webdriver.Firefox(firefox_profile=fp,executable_path=r'E:\Python37\geckodriver.exe')
    driver.implicitly_wait(20)  #隐性等待，最长等20秒

    #打开airbnb的网页
    for i in range(0,1):  #设置获取多页房子数据
        driver.get('https://www.airbnb.com/s/ShenZhen--China/homes?items_offset={}'.format(str(i*18))) #items_offset这个参数在url以18的增长
        #找出页面所有出租房
        time.sleep(3)
        all_list = driver.find_elements_by_css_selector('div._gig1e7')
        time.sleep(3)
        print('第{}页房子数据'.format(str(i+1)))
        #对于每一间出租房
        for each_house in all_list:
            #找到房子名称
            name = each_house.find_element_by_css_selector('div._qrfr9x5').text
            # time.sleep(3)
            #房子价格
            price = each_house.find_element_by_css_selector('div._1orel7j7').text.replace("价格","").replace("\n","")
            # time.sleep(3)
            #评价数量和分数
            try:
                comment = each_house.find_element_by_css_selector('div._13o4q7nw')
                # time.sleep(3)
                comment = comment.text
                fenshu = comment.split(' · ')[0]
                connent_num = comment.split(' · ')[1]
            except:
                fenshu = '暂无评论'
                connent_num = 0
            #房屋类型，床数量
            details = each_house.find_element_by_css_selector('span._faldii7').text
            # time.sleep(3)
            house_type = details.split(' · ')[0]
            bad_num = details.split(' · ')[1]

            homes_details = '房子名称:{}|房子价格:{}|房屋类型:{}|床数量:{}|评价数量:{}|好评分数:{}\n'.format(name,price,house_type,bad_num,connent_num,fenshu)
            print(homes_details)
            time.sleep(5)
            write_data(homes_details) #调用 write_data() 函数写入数据，并保存


def write_data(data_string):
    '''把数据写入txt文件中'''
    with open('homes.txt','a+',encoding='utf-8') as f:
        f.write(data_string)


if __name__ == '__main__':
    get_homes()


