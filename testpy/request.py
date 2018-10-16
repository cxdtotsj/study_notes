import requests

url = "https://dt-dev.arctron.cn/api/user/login"
data = {"email":"admin@admin",
        "password":"abc123"}

res = requests.post(url,data).json()
print(res)