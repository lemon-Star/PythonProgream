import requests

req=requests.get("http://httpbin.org/get")
print(type(req))
print(req.text)
