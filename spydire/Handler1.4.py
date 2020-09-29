import http.cookiejar
import urllib.request

fileName="cookie.txt"
cookie=http.cookiejar.LWPCookieJar()
#加载cookie
cookie.load(fileName,ignore_expires=True,ignore_discard=True)
#装在handler
handler=urllib.request.HTTPCookieProcessor(cookie)
#获取opener
opener=urllib.request.build_opener(handler)
response=opener.open("https://www.baidu.com")
print(response.read().decode('utf-8'))