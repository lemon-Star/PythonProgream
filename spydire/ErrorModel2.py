from urllib import request,error

try:
    response=request.urlopen("https://www.baidu.com/index.html",timeout=0.01)
except error.HTTPError as e:
    print("this si HTTPERRPR")
except error.URLError as e :
    print("this is urlERROR")
else :
    print("SUCCESS")