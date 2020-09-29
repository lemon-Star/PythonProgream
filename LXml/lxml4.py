from lxml import etree

#也可以通过文本进行解析
html=etree.parse('lxml3.html',etree.HTMLParser())
#result=html.xpath('//ul//a')   #ul 下的全部a  //ul/a  ul下没有直接子节点a 所以是空的
#result=html.xpath('//ul//a')
result=html.xpath('//li[@class="item-1"]/a/text()')
print(result)
