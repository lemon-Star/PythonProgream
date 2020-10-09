from bs4 import BeautifulSoup

html='''
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's Story</b></p>
<p class="story">Once upon a time here were three little sisters: and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie --></a>，
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the botttom of a well.
</p>
<p class="story">....</p>
</body>
</html>
'''
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())  #缩紧格式输出    对于不标准的HTML字符串可以自动更正格式，不是这个方法，而是初始化BeautifulSoup时候就解决了
#获取节点信息  利用name属性获取节点名称，选取title节点，
print(''' 利用name属性获取节点名称，选取title节点，获取name属性，获得名称  soup.title.name = ''')
print(soup.title.name)

print('''
 获取属性，每个节点可能有多个属性，比如id和class等，选择这个节点元素之后，可以调用attrs获取所有属性
''')
print(soup.p.attrs)
print(soup.p.attrs['name'])

print('''
获取内容，可以利用string属性获取节点元素包含的文本内容，比如获取第一个p节点的文本:soup.p.string==
''')
print(soup.p.string)


