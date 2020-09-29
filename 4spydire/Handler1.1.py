import http.cookiejar
import urllib.request

#cookie 先创建handler，之后用创建的handler生成opener
cookie = http.cookiejar.CookieJar();
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open("https://www.baidu.com")
for item in cookie:
    print(item.name + "="+item.value)