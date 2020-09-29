import http.cookiejar
import urllib.request

#cookie以文本的形式保存下来
fileName="/Users/star/PycharmProjects/pythonProject/spydire/cookie.txt"
cookie=http.cookiejar.LWPCookieJar(fileName)
#cookie = http.cookiejar.CookieJar();
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)

#LWP-Cookies-2.0
#Set-Cookie3: BAIDUID="7074EAD94A52B7ECDFD297609412A977:FG=1"; path="/"; domain=".baidu.com"; path_spec; domain_dot; expires="2021-09-24 01:04:53Z"; comment=bd; version=0
#Set-Cookie3: BIDUPSID=7074EAD94A52B7EC1554A0CC5932C325; path="/"; domain=".baidu.com"; path_spec; domain_dot; expires="2088-10-12 04:19:00Z"; version=0
#Set-Cookie3: PSTM=1600909493; path="/"; domain=".baidu.com"; path_spec; domain_dot; expires="2088-10-12 04:19:00Z"; version=0
#Set-Cookie3: BD_NOT_HTTPS=1; path="/"; domain="www.baidu.com"; path_spec; expires="2020-09-24 01:09:53Z"; version=0
