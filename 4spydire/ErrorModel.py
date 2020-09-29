from urllib import request,error

#避免抛出不期望的错误
try:
    response=request.urlopen("http://sssdfsdfsd.com")
except error.URLError as e :
    print(e.reason)