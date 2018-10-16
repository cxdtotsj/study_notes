import requests
from bs4 import BeautifulSoup


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

# res = requests.get("https://book.douban.com/")
# res.encoding = res.apparent_encoding

# soup = BeautifulSoup(res.text,'lxml')

# book_list = soup.select(".cover")


res = requests.get("http://jandan.net/pic")

res.encoding = res.apparent_encoding

soup = BeautifulSoup(res.text,'lxml')

pic_list = soup.select(".text")


# soup2 = BeautifulSoup(pic_list[0],'lxml')
print(pic_list[0])