import requests
import json

# url = "https://dt-dev.arctron.cn/api/user/login"
# data = {"email":"admin@admin",
#         "password":"abc123"}

# res = requests.post(url,data).json()
# print(res)

r = requests.get('https://api.github.com/events')
print(r.content)

dict_json = json.loads(r.content)
print(dict_json)