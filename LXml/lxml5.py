from lxml import etree

#属性获取  获取所有li节点下所有a节点下 href的属性
html=etree.parse('lxml3.html',etree.HTMLParser())
result=html.xpath('//li/a/@href')
print(result)