import requests
import json
import csv
import os
from fake_useragent import UserAgent
import pandas as pd


class SpiderMaoyan:

    headers = {
        "User-Agent": UserAgent(verify_ssl=False).random,
        "Host": "m.maoyan.com",
        "Referer": "http://m.maoyan.com/movie/1217236/comments?_v_=yes"
    }
    
    def __init__(self,url,time):
        self.url = url
        self.time = time
    
    # 发送 get 请求
    def get_json(self):
        res_comment = requests.get(self.url,headers=self.headers).json()
        return res_comment
    
    # 获取需要的数据

    def get_data(self,res_comment):
        json_comment = res_comment["cmts"]
        print(len(json_comment))
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
            list_one = [self.time, nickName, gender,
                cityName, userLevel, score, content]
            list_info.append(list_one)
        self.file_do(list_info)
    
    def file_do(self,list_info):
        file_name = r"D:\Testfan\study_notes\learn_python3\spider_obj\maoyan.csv"
        file_size = os.path.getsize(file_name)
        if file_size == 0:
            # 表头
            name = ['评论日期', '评论者昵称', '性别', '城市', '用户等级', '评分', '评论内容']
            # 建立 DataForm 对象
            file_test = pd.DataFrame(columns=name,data=list_info)
            # 写入数据
            file_test.to_csv(file_name,encoding='utf-8-sig',index='')
        else:
            with open(file_name,"a+",encoding='utf-8-sig',newline='') as file_test:
                # 追加到文件
                writer_content = csv.writer(file_test)
                # 写入文件
                writer_content.writerows(list_info)

def spider_maoyan():
    # 猫眼电影短评接口
    offset = 0
	# 电影是2018.9.21上映的
    startTime = '2018-09-21'
    day = [22,23,24,25,26,27,28,29,30,1,2,3,4,5,6]
    j = 0
    page_mun = int(20000/15)
    for i in range(page_mun):
        comment_api = "http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={}&startTime={}%2009%3A33%3A46".format(offset,startTime)
        s0 = SpiderMaoyan(comment_api,startTime)
        json_comment = s0.get_json()
        if json_comment["total"] == 0:
            if j < 9:
                startTime = '2018-09-%d'%day[j]
            elif j >= 9 and j < 15:
                startTime = '2018-09-%d'%day[j]
            else:
                break
            offset = 0
            j = j + 1
            continue
        s0.get_data(json_comment)
        offset = offset + 15


        
if __name__ == 'main':
	spider_maoyan()