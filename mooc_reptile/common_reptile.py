import requests

def comm_reptile():
    try:
        r = requests.get("https//www.baidu.com",timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"