import requests

data={
    'name':'Bob',
    'password':'1111'
}
url='http://httpbin.org/post'
r=requests.post(url,data=data)
print(r.text)
