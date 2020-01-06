# encding:utf-8

'''
@author: Hollow
@file: get_movie_name.py
@time: 2019-10-28 15:10

'''

import requests
from bs4 import BeautifulSoup

def get_movie():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                'Host':'movie.douban.com'
    }
    link = 'https://movie.douban.com/top250?start='

    movies_list = []
    for i in range(0,10):
        url = link + str(i *25)
        r = requests.get(url = url,headers=headers,timeout= 10)
        # print(r.status_code,r.url)
        soup = BeautifulSoup(r.text,"html.parser")
        div_list = soup.find_all('div',class_ = 'hd')  #找到hd下面所有div标签
        # print(div_list)
        for item in div_list:
            movies = item.a.span.text.strip()
            movies_list.append(movies)
    return movies_list



if __name__ == '__main__':
    result = get_movie()
    print(result)
