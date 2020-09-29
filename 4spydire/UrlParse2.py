from urllib.parse import urlencode

#通过rulecode序列化成get请求的参数
params={
    "userName":"bob",
    "passWord":"a111111"
}
getParams = urlencode(params)
print(getParams)
