from bs4 import BeautifulSoup
import re
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
#可以根据节点名称来选择
print(soup.find_all(name='p'))
#根据文本选择
print(soup.find_all(text=re.compile('Once')))