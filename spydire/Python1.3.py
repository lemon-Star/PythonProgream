import urllib.request
import urllib.error


# url请求参数加上 timeout请求超时时间  报错： urllib.error.URLError: <urlopen error timed out>
#response: object= urllib.request.urlopen("http://httpbin.org/get" ,timeout=0.1)
#print(response.read())


#针对超时问题，我们可以cache异常，跳过本次抓取
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    print(e.reason);
