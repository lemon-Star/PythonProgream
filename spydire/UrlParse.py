from urllib.parse import urlparse

result=urlparse("http://www.baidu.com#?id=555")
print((type(result),result))