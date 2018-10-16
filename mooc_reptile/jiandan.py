import requests
from bs4 import BeautifulSoup
import bs4

path = "D:\123.jpg"


res = requests.get("http://ww3.sinaimg.cn/mw600/006XNEY7gy1fw8vnybo3xj31hc140trx.jpg")
res.encoding = res.apparent_encoding
# with open(path,"wb") as fp:
#     fp.write(res.content)

html = res.text
soup = BeautifulSoup(html,'html.parser')

uls = soup.findAll("img")

print(uls)



