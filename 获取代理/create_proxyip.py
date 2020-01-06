# encding:utf-8

'''
@author: Hollow
@file: create_proxyip.py
@time: 2019-10-18 16:02

'''
import bs4
from bs4 import BeautifulSoup
import requests
from urllib import request,error
import threading


lock = threading.Lock()  #线程锁
inFile = open('ip.txt')
verifiedtxt = open('verified.txt')

def get_proxy(url):
    '''获取代理ip'''
    global headers
    headers = {
        "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    }

    for i in range(1,11):  #获取1--10页
        url = url + str(i)
        # print(url)
        res = requests.get(url,headers)
        html = res.text
        soup = BeautifulSoup(html,"lxml")
        # print(html)
        #获取 table class="table table-bordered table-striped"下的所有 tr的标签
        trs = soup.find("div",id = "list").find_all("tr") # 这里获得的是一个list列表
        try:
            if isinstance(trs,bs4.Tag):
            #循环这个列表
                for item in trs[1:]:
                    tds = item.find_all("td")  #获取所有td标签的内容
                    # print(tds)
                    ip = tds[0].text.strip()
                    port = tds[1].text.strip()
                    k = tds[2].text.strip()
                    mold = tds[3].text.strip()
                    location = tds[4].text.strip()
                    speed = tds[5].text.strip()
                    end_check_time = tds[6].text.strip()
                    print('{}|{}|{}|{}|{}|{}|{}'.format(ip,port,k,mold,location,speed,end_check_time))
                    result = '{}|{}|{}|{}|{}|{}|{}\n'.format(ip,port,k,mold,location,speed,end_check_time)

                    with open('ip.txt','a',encoding='utf-8') as f:
                        f.write(result)
        except Exception as e:
            return e

def verify_proxy_list():

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0 : break
        line = ll.strip().split('|')
        ip = line[1]
        port = line[2]
        realip = ip+':'+port
        code = verify_proxy(realip)
        if code == 200:
            lock.acquire()
            print("---Success:" + ip + ":" + port)
            with open('verified.txt','a',encoding='utf-8') as f:
                f.write(ll + "\n")
            lock.release()
        else:
            print("---Failure:" + ip + ":" + port)


def verify_proxy(ip):
    '''
    验证代理的有效性
    '''
    requestHeader = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
    }
    url = "http://www.baidu.com"
    # 填写代理地址
    proxy = {'http': ip}
    # 创建proxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建ｏｐｅｎｅｒ
    proxy_opener = request.build_opener(proxy_handler)
    # 安装opener
    request.install_opener(proxy_opener)

    try:
        req = request.Request(url, headers=requestHeader)
        rsq = request.urlopen(req, timeout=5.0)
        code = rsq.getcode()
        return code
    except error.URLError as e:
        return e

if __name__ == '__main__':
    tmp = open('ip.txt', 'w')
    tmp.write("")
    tmp.close()
    tmp1 = open('verified.txt', 'w')
    tmp1.write("")
    tmp1.close()
    get_proxy("https://www.kuaidaili.com/free/inha/")
    get_proxy("https://www.kuaidaili.com/free/intr/")

    all_thread = []
    for i in range(30):
        t = threading.Thread(target=verify_proxy_list)
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()

    inFile.close()
    verifiedtxt.close()











# if __name__ == "__main__":
#     get_proxy('https://www.kuaidaili.com/free/inha/')



# from bs4 import BeautifulSoup
# import requests
# from urllib import request,error
# import threading


# inFile = open('proxy.txt')
# verifiedtxt = open('verified.txt')
# lock = threading.Lock()  #线程锁
# def getProxy(url):
#     # 打开我们创建的txt文件
#     proxyFile = open('proxy.txt', 'a')
#     # 设置UA标识
#     headers = {
#         'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit '
#                       '/ 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36'
#     }
#     # page是我们需要获取多少页的ip，这里我们获取到第９页
#     for page in range(1, 10):
#         # 通过观察ＵＲＬ，我们发现原网址+页码就是我们需要的网址了，这里的page需要转换成str类型
#         urls = url+str(page)
#         # 通过requests来获取网页源码
#         rsp = requests.get(urls, headers=headers)
#         html = rsp.text
#         # 通过BeautifulSoup，来解析html页面
#         soup = BeautifulSoup(html)
#         # 通过分析我们发现数据在　id为ip_list的table标签中的tr标签中
#         trs = soup.find('table', id='ip_list').find_all('tr') # 这里获得的是一个list列表
#         # 我们循环这个列表
#         for item in trs[1:]:
#             # 并至少出每个tr中的所有td标签
#             tds = item.find_all('td')
#             # 我们会发现有些img标签里面是空的，所以这里我们需要加一个判断
#             if tds[0].find('img') is None:
#                 nation = '未知'
#                 locate = '未知'
#             else:
#                 nation = tds[0].find('img')['alt'].strip()
#                 locate = tds[3].text.strip()
#             # 通过td列表里面的数据，我们分别把它们提取出来
#             ip = tds[1].text.strip()
#             port = tds[2].text.strip()
#             anony = tds[4].text.strip()
#             protocol = tds[5].text.strip()
#             speed = tds[6].find('div')['title'].strip()
#             time = tds[8].text.strip()
#             # 将获取到的数据按照规定格式写入txt文本中，这样方便我们获取
#             proxyFile.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol, speed, time))
#
#
# def verifyProxyList():
#
#     verifiedFile = open('verified.txt', 'a')
#
#     while True:
#         lock.acquire()
#         ll = inFile.readline().strip()
#         lock.release()
#         if len(ll) == 0 : break
#         line = ll.strip().split('|')
#         ip = line[1]
#         port = line[2]
#         realip = ip+':'+port
#         code = verifyProxy(realip)
#         if code == 200:
#             lock.acquire()
#             print("---Success:" + ip + ":" + port)
#             verifiedFile.write(ll + "\n")
#             lock.release()
#         else:
#             print("---Failure:" + ip + ":" + port)
#
#
#
#
# def verifyProxy(ip):
#     '''
#     验证代理的有效性
#     '''
#     requestHeader = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
#     }
#     url = "http://www.baidu.com"
#     # 填写代理地址
#     proxy = {'http': ip}
#     # 创建proxyHandler
#     proxy_handler = request.ProxyHandler(proxy)
#     # 创建ｏｐｅｎｅｒ
#     proxy_opener = request.build_opener(proxy_handler)
#     # 安装opener
#     request.install_opener(proxy_opener)
#
#     try:
#         req = request.Request(url, headers=requestHeader)
#         rsq = request.urlopen(req, timeout=5.0)
#         code = rsq.getcode()
#         return code
#     except error.URLError as e:
#         return e
#
# if __name__ == '__main__':
#     tmp = open('proxy.txt', 'w')
#     tmp.write("")
#     tmp.close()
#     tmp1 = open('verified.txt', 'w')
#     tmp1.write("")
#     tmp1.close()
#     getProxy("http://www.xicidaili.com/nn/")
#     getProxy("http://www.xicidaili.com/nt/")
#     getProxy("http://www.xicidaili.com/wn/")
#     getProxy("http://www.xicidaili.com/wt/")
#
#     all_thread = []
#     for i in range(30):
#         t = threading.Thread(target=verifyProxyList)
#         all_thread.append(t)
#         t.start()
#
#     for t in all_thread:
#         t.join()
#
#     inFile.close()
#     verifiedtxt.close()