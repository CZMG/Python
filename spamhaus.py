#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WYF
2019/7/19
此工具用于爬取spamhaus网页的指定数据，保存为xls格式的工作簿。
"""

import re
import requests
import bs4
import os
import xlwt

url = 'https://www.spamhaus.org/sbl/listings/chinanet-js'

ip = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}\/\d{2}')

content_SBL = []
content_time = []
content_ip = []

data_url = requests.get(url)
soup = bs4.BeautifulSoup(data_url.text，"html.parser")
content = soup.find_all('span',class_='body')

for i in range(len(content)):
    temp = content[i].get_text()

    if "SBL" in temp:
        content_SBL.append(temp)
    elif "GMT" in temp:
        content_time.append(temp)
    else:
        ip_temp = ip.search(temp)

        if ip_temp is not None:
            content_ip.append(ip_temp.group())

content_SBL[0] = "SBL"
content_time.insert(0, "Time")
content_ip.insert(0, "IP")

dir_user = os.path.join(os.path.expanduser("~"), 'Desktop') 
os.chdir(dir_user)
#file_ip = dir_user + '\\ip.txt'
#file_sbl = dir_user + '\\sbl.txt'
#file_time = dir_user + '\\time.txt'
#
#if os.path.exists(file_ip):
#    os.remove(file_ip)
#elif os.path.exists(file_sbl):
#    os.remove(file_sbl)
#elif os.path.exists(file_time):
#    os.remove(file_time)
#
#f_ip = open(file_ip,'w+')
#for i in content_ip:
#    f_ip.write(i+'\n')
#f_ip.close()
#
#f_sbl = open(file_sbl,'w+')
#for j in content_SBL[1:]:
#    f_sbl.write(j+'\n')
#f_sbl.close()
#
#f_time = open(file_time,'w+')
#for k in content_time:
#    f_time.write(k+'\n')
#f_time.close()

file_name = 'spamhaus.xls'
wenjian = dir_user+'\\'+file_name
if os.path.exists(wenjian):
    os.remove(wenjian)

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Data')
def xwrite(file_list,num):
    for i in range(len(file_list)):
        worksheet.write(i,num,label=file_list[i])
xwrite(content_SBL,0)
xwrite(content_time,1)
xwrite(content_ip,2)
workbook.save(file_name)


