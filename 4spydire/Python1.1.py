import urllib.request
import urllib.parse
import json

# 学习post请求，带上data参数，则表示post请求，但是需要转码来传入
data = bytes(urllib.parse.urlencode({'world': 'hello World'}), encoding='UTF-8');
response = urllib.request.urlopen("http://httpbin.org/post", data=data);
# print(json.load(response.read()));
print(response.read())


