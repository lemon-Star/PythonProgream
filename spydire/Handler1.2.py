import http.cookiejar
import urllib.request

#cookie以文本的形式保存下来
fileName="/Users/star/PycharmProjects/pythonProject/spydire/cookie.txt"
cookie=http.cookiejar.MozillaCookieJar(fileName)
#cookie = http.cookiejar.CookieJar();
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

#.baidu.com	TRUE	/	FALSE	1632444894	BAIDUID	43CBA23F6F4CA3BD7EA603F1D6EC1825:FG=1
#.baidu.com	TRUE	/	FALSE	3748392541	BIDUPSID	43CBA23F6F4CA3BDC3120C3AA8EE2D83
#.baidu.com	TRUE	/	FALSE	3748392541	PSTM	1600908894
#www.baidu.com	FALSE	/	FALSE	1600909194	BD_NOT_HTTPS	1
