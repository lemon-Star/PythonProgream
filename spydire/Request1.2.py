import urllib.request
import urllib.parse

url="https://httpbin.org/post"
headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
     'Host':'httpbin.org'
}
dict={
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict),encoding='utf-8')
request=urllib.request.Request(url=url,headers=headers,data=data,method='POST')
response=urllib.request.urlopen(request,timeout=10)
print(response.read(),'UTF-8')

