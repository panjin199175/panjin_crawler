# encding:utf-8

'''
@author: Hollow
@file: get_comment.py
@time: 2019-10-29 10:05

'''

#通过selenium模拟浏览器爬取数据

from selenium import webdriver
import time


#控制 css
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.stylesheet",2)
#限制图片的加载
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.image",2)
#限制javascript的加载
fp = webdriver.FirefoxProfile()
fp.set_preference("javascript.enabled",False)

driver = webdriver.Firefox(firefox_profile=fp,executable_path=r'E:\Python37\geckodriver.exe')
driver.implicitly_wait(20)  #隐性等待，最长等20秒
driver.get('http://www.santostang.com/2018/07/04/hello-world/')
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #下滑到页面的底部
time.sleep(2)

for i in range(1,4):
    if i < 12:  #判断页数小于12的，1-11页走下面的逻辑
        #转换iframe表单里面
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
        time.sleep(8)
        #在找页数按钮，点击
        driver.find_element_by_xpath('//*[@id="list"]/div[11]/button[{}]'.format(str(i))).click()
        time.sleep(5)
        comment = driver.find_elements_by_css_selector('div.reply-content')
        time.sleep(3)
        for item in comment:
            content =item.find_element_by_tag_name('p') #获取p标签里的文本内容
            time.sleep(3)
            print(content.text)
        #切出iframe框架
        driver.switch_to.default_content()
        time.sleep(2)
    else:
        t = i - 9
        #转换iframe表单里面
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
        time.sleep(8)
        #在找页数按钮，点击
        driver.find_element_by_xpath('//*[@id="list"]/div[11]/button[{}]'.format(str(t))).click()
        time.sleep(5)
        comment = driver.find_elements_by_css_selector('div.reply-content')
        time.sleep(3)
        for item in comment:
            content =item.find_element_by_tag_name('p')
            time.sleep(3)
            print(content.text)
        #切出iframe框架
        driver.switch_to.default_content()
        time.sleep(2)



