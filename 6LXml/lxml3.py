from lxml import etree

#也可以通过文本进行解析
html=etree.parse('lxml3.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))