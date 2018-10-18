'''
data:2018-10-16
goal: 爬取猫眼《悲伤逆流成河》影评
'''

# 猫眼 url
# http://maoyan.com/films/1217236

import requests
import json
import csv
import os
from fake_useragent import UserAgent
import pandas as pd


# class Spidermaoyan:
#     headers = {
#         "User-Agent":UserAgent(verify_ssl=False).random,
#         "Host":"m.maoyan.com",
#         "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
#     }

#     def __init__(self,url,time):
#         self.url = url
#         self.time = time

#     # 发送get请求


headers = {
    "User-Agent": UserAgent(verify_ssl=False).random,
    "Host": "m.maoyan.com",
    "Referer": "http://m.maoyan.com/movie/1217236/comments?_v_=yes"
}

# 猫眼电影短评接口
offset = 0

# 日期，上映未 2018.9.21
start_time = '2018-09-21'
comment_api = "http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={}&startTime={}%2009%3A33%3A46".format(
    offset, start_time)
# 发送请求

res_comment = requests.get(comment_api, headers=headers).json()
# print(res_comment.json())

json_comment = res_comment["cmts"]
list_info = []
for data in json_comment:
    cityName = data["cityName"]
    content = data["content"]
    if "gender" in data:
        gender = data["gender"]
    else:
        gender = 0
    nickName = data["nickName"]
    userLevel = data["userLevel"]
    score = data["score"]
    list_one = [start_time, nickName, gender,
                cityName, userLevel, score, content]
    list_info.append(list_one)
# print(list_info)

file_name = r"D:\Testfan\study_notes\learn_python3\spider_obj\maoyan.csv"
file_size = os.path.getsize(file_name)
if file_size == 0:
    # 表头
    name = ['评论日期', '评论者昵称', '性别', '城市', '用户等级', '评分', '评论内容']
    # 建立DataFrame对象
    file_test = pd.DataFrame(columns=name, data=list_info)
    # 数据写入
    file_test.to_csv(file_name, encoding='utf-8-sig', index=False)
else:
    with open(file_name,"a+",encoding="utf-8-sig",newline='') as file_test:
        # 追加到文件后面
        writer = csv.writer(file_test)
        # 写入文件
        writer.writerows(list_info)