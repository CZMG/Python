#!/usr/bin/env python3

import bs4
import re
import requests
import os

# 用户信息输入
print("此程序用于下载笔趣阁的小说，网站地址：http://www.biquge.com.tw/。")
bookname = input("请输入小说名： ")
userurl = input("请输入小说首页的链接： ")
directory = input("请输入小说的保存目录： ")

bqgurl = "http://www.biquge.com.tw"
lj = directory+bookname

os.mkdir(lj)
os.chdir(lj)

# 地址池
url_pool = []

# 获取小说每章节的地址
r = requests.get(userurl)
r.encoding = 'gbk'
# soup = bs4.BeautifulSoup(r.text, from_encoding='gbk')
soup = bs4.BeautifulSoup(r.text,"html.parser")
# soup.find_all('a',href=re.compile(r'/\d.\d+/\d+.html'))
for nurl in soup.find_all('a', href=re.compile(r'/\d.\d+/\d+.html')):
    wurl = bqgurl + nurl['href']
    url_pool.append(wurl)
print(bookname+"一共"+str(len(url_pool))+"章。")
print("下载中......")
# 下载每章节小说并写入文件保存
for url in url_pool:
    book = requests.get(url)
    book.encoding = 'gbk'
#    nsoup = bs4.BeautifulSoup(book.text.replace('<br />', ''), from_encoding='gbk')
    nsoup = bs4.BeautifulSoup(book.text.replace('<br />', ''),"html.parser")
    zjname = nsoup.find(class_="bookname").h1.get_text()+'.txt'
    temp = nsoup.select('#content')[0]
    content = re.sub('\s+', '\r\n\t', temp.text).strip('\r\n')
    f = open(zjname, 'w+')
    f.write(content)
    f.close()


print("下载完成！")
