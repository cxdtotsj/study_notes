#!/bin/env/python
# -*- encoding: UTF-8 -*-
import requests, os, re, urlparse
from bs4 import BeautifulSoup
from pprint import pprint

r = requests.get("https://www.pexels.com/")
data = r.text
soup = BeautifulSoup(data, "lxml")
for link in soup.find_all('img'):
    img_src = link.get('src')
    if not img_src:
        continue
    #img_name =  = os.path.split(img(img_src)[1]
    if not re.search('https://',img_src):
        # pprint(img_src)
        continue
    #    pprint(img_src)
    # pprint(img_src)
    parsed_link = urlparse.urlparse(img_src)
    img_name = (os.path.basename(parsed_link.path))
    # pprint(img_name)
    r2 = requests.get(img_src)
    save_dir = './tiny/'
    with open(save_dir + img_name, 'wb') as f:
           f.write(r2.content)