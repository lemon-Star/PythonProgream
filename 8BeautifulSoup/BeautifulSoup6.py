from bs4 import BeautifulSoup
#class选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="elements">Foo</li>
            <li class="elements">Bar</li>
            <li class="elements">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="elements">Foo</li>
            <li class="elements">Bar</li>
        </ul>
    </div>
</div>
'''
soup=BeautifulSoup(html,'lxml')
print('''------------''')
print(soup.select('.panel .panel-heading'))
print('''------------选择ul 下的li''')
print(soup.select('ul li'))
print('''------------id是list2下面的elements节点''')
print(soup.select('#list-2 .elements'))
print('''
------------select支持嵌套选择，例如选择所有ul节点，在遍历每个ul节点，选择其li节点
''')
for ul in soup.select('ul'):
    print(ul.select('li'))

print('''
----------获取属性信息,我们知道节点类型是Tag类型，所以获取属性还可以用原来的方式
''')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
    print(ul['class'])

print('''
-----------获取文本信息 两种方式获取的信息一致的：
''')

for li in soup.select('li'):
    print("get Test():"+li.get_text())
    print("string:"+li.string)