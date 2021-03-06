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
print(soup.prettify())  #缩紧格式输出    对于不标准的HTML字符串可以自动更正格式，不是这个方法，而是初始化BeautifulSoup时候就解决了
print(soup.title)
print(soup.title.string)