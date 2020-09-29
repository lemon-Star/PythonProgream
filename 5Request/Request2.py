import requests

req=requests.get("https://www.baidu.com")
print(type(req))
print(req.status_code)
print(req.text)