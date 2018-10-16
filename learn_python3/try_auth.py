import requests
from requests.auth import HTTPBasicAuth,HTTPDigestAuth

url = "https://github.com"

# auth = HTTPDigestAuth("xdchenadmin@admin","123456")

auth = HTTPBasicAuth("xdchenadmin@admin","123456")

print(auth)

res = requests.get(url,auth=("cxdtotsj@163.com","cxdaitsj19900527"))
print(res.text)