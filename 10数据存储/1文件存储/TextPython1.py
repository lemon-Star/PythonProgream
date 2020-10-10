import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup



print('''
利用request获取网页上源代码，使用pyqueyr解析库解析，提取标题等内容
''')

url="https://www.zhihu.com/explore"
headers={
    'cookie':'_zap=bed9c2bc-2125-469a-a236-ca430fafd467; d_c0="APAar4HzxhGPTq7uG39OeQq7sRz4J4T2k_4=|1598189164"; _ga=GA1.2.1447417251.1598189167; capsion_ticket="2|1:0|10:1601022422|14:capsion_ticket|44:ZWI1YWE2NTUwODhiNGZhNjhlZmExZDM2MzVkOWFmM2Y=|b372a065594a163ffa1e9cb4255a1143bd346aafd6589ca8139be5616f258895"; z_c0="2|1:0|10:1601022445|4:z_c0|92:Mi4xN2N3WkJ3QUFBQUFBOEJxdmdmUEdFU1lBQUFCZ0FsVk43ZmRhWUFDbFRYT3loLTdMcmJHRm5fZm5naXQwOXVUcXhR|472dd09c39e4ec3706737d724f7409d88c9bf251afecc9984886edc87089ef7e"; tst=r; q_c1=c60ed278a11d4b469d6d4312f0567e56|1601263010000|1601263010000; _xsrf=1965f318-9469-48eb-848f-85c378f9979d; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1601022755,1601026203,1601263010,1602231594; _gid=GA1.2.162699746.1602231594; SESSIONID=FstN3XvMgi83DNqZLqyQAShf2chvt4aQ5muTKixcIdp; JOID=VlwVAE0hKlRBXECTYyZ4BojZtFd2Z10jCm0Y4S1EQ2hxHQziPQ8w0hleRJRl9YvG0d2DcSAX2hl8iJydOEQje-s=; osd=V10SAEwgK1NBXUGSZCZ5B4netFZ3ZlojC2wZ5i1FQml2HQ3jPAgw0xhfQ5Rk9IrB0dyCcCcX2xh9j5ycOUUke-o=; __utmc=51854390; __utmz=51854390.1602232154.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.110-1|2=registration_date=20171231=1^3=entry_date=20171231=1; __utma=51854390.1447417251.1598189167.1602232154.1602289713.2; __utmb=51854390.0.10.1602289713; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1602289983; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1602289985|1602289710',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
html=requests.get(url,headers=headers).text
print(html)
soup=BeautifulSoup(html,'lxml')
print(soup.text)
for ul in soup.select('explore-feed feed-item'):
    print(ul)