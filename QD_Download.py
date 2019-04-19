import bs4
import requests
import os
import re
import w3lib.html

#用户信息输入
print("此程序用于下载起点中文网的小说，网站地址：https://www.qidian.com/。")
novelname = input("请输入小说名： ")
novelurl = input("请输入小说首页的链接： ")
directory = input("请输入小说的保存目录： ")

qdurl = "https://www.qidian.com/"
lj = directory+novelname

os.mkdir(lj)
os.chdir(lj)

#获取分URL
chapterUrls = []
chapterNames = []

r = requests.get(novelurl)
r.encoding = 'UTF-8'
soup = bs4.BeautifulSoup(r.text, "html.parser")
div = soup.find_all('div', class_='volume')
for i in range(len(div)):
    li = div[i].find_all('li')
    for j in range(len(li)):
        a = li[j].find_all('a')
        html = bs4.BeautifulSoup(str(a), 'html.parser')
        # 章节url
        chapterUrls.append('https:' + str(html.a.get('href')))
        # 章节名
        chapterNames.append(html.a.string)
print("本书一共", len(chapterNames), '章。')
print("开始下载...")


#进入各章节，下载内容
number = 0
for url in chapterUrls:
    book = requests.get(url)
    book.encoding = "utf-8"
    nsoup = bs4.BeautifulSoup(book.text, "html.parser")
    content = nsoup.find_all('div', class_='read-content j_readContent')
    contents = w3lib.html.remove_tags(str(content).replace(u'<p>', u'\n'))
    zjname = str(chapterNames[number]) + '.txt'
    number += 1
    f = open(zjname,'w+')
    f.write(contents)
    f.close()

print("下载完成！")
