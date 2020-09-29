from lxml import etree

#属性获取 属性多值匹配
text="<li class='li li-first' name='linkName'><a href='link.html'>first item</a><>/li>"
html=etree.HTML(text)
result=html.xpath('//li/a/text()')
print(result)