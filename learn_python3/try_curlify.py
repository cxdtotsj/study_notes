import curlify
import requests

res = requests.get("https://www.baicu.com")
print(curlify.to_curl(res.request))