from lxml import etree

text='''
<div>
  <ul>
    <li class="item-1"><a href="link1.html">first item</a></li>
    <li class="item-2"><a href="link2.html">second item</a>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fouuth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
  </ul>
</div>
'''
html=etree.HTML(text)#节点会被补全 li  自动添加了body html节点
result = etree.tostring(html)
print(result.decode('utf-8'))