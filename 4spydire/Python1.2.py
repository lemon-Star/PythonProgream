import urllib.request


# url请求参数加上 timeout请求超时时间  报错： urllib.error.URLError: <urlopen error timed out>
response: object= urllib.request.urlopen("http://httpbin.org/get" ,timeout=0.1)
print(response.read())