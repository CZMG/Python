#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WYF

"""

import re
import requests
import bs4
import os

url = 'https://www.spamhaus.org/sbl/listings/chinanet-js'
ip = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}\/\d{2}')

content_SBL = []
content_time = []
content_ip = []

data_url = requests.get(url)
soup = bs4.BeautifulSoup(data_url.text)
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

dir_user = os.path.join(os.path.expanduser("~"), 'Desktop') 
file_ip = dir_user + '\\ip.txt'
file_sbl = dir_user + '\\sbl.txt'
file_time = dir_user + '\\time.txt'

f_ip = open(file_ip,'w+')
for i in content_ip:
    f_ip.write(i+'\n')
f_ip.close()

f_sbl = open(file_sbl,'w+')
for j in content_SBL[1:]:
    f_sbl.write(j+'\n')
f_sbl.close()

f_time = open(file_time,'w+')
for k in content_time:
    f_time.write(k+'\n')
f_time.close()
