import requests
import json

# url = "https://dt-dev.arctron.cn/api/user/login"
# data = {"email":"admin@admin",
#         "password":"abc123"}

# res = requests.post(url,data).json()
# print(res)

r = requests.get('https://www.baidu.com')
r.encoding = r.apparent_encoding
print(r.text)
