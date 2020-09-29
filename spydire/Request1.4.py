from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

#代理模式
proxy_handler=ProxyHandler({
    'http':'173.82.243.6:12906'
})
opener=build_opener(proxy_handler)
response=opener.open("https://www.baidu.com")
print(response.read())
