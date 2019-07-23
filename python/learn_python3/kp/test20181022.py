import requests

url = "http://api.douban.com/v2/movie/top250"
data = {"start":1,"count":25}
r = requests.get(url,data)
print(r)
content = r.json()
print(content)