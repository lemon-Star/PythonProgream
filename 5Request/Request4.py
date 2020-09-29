import requests

#传入参数来试试
#req=requests.get("http://httpbin.org/get?name=germey&age=22")
param={
    'name':'germey',
    'age':'22'
}
url='http://httpbin.org/get'
req=requests.get(url,params=param)
print(type(req))
print(req.text)
print(req.json())