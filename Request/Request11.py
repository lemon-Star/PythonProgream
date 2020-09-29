from requests import Session,Request


#引入Request，然后将url，data，headers参数构造了一个Request对象
url="http://httpbin.org/post"
data={
    'name':'Germery'
}
headers={
    'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2473.116 Safari/537.36'
}
s=Session()
req = Request(url=url,headers=headers,data=data,method='POST')
#req = Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)

