'''
data:2018-10-16
goal: 爬取猫眼《悲伤逆流成河》影评
'''

# 猫眼 url
# http://maoyan.com/films/1217236

import requests
import json
from fake_useragent import UserAgent

headers = {
    "User-Agent":UserAgent(verify_ssl=False).random,
    "Host":"m.maoyan.com",
    "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
}

