from urllib.parse import quote
import urllib.request
from urllib.parse import unquote

#将内容转化成URL编码的格式
keyWords="壁纸"
url = "https://www.baidu.com/s?wd="+quote(keyWords)
print(url)
response=urllib.request.urlopen(url)

#解码格式
print(unquote(url))