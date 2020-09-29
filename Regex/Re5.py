import re

#search可以返回匹配正则表达式的第一个内容，匹配到就不继续匹配了，findAll则可以获取所有
context='''
<div id="song-list">
  <h2 class="title">经典老歌</h2>
  <p class="introduction">经典老歌列表</p>
  <ul id ="list" class="list-group">
  	<li data-view="2">一路上有你</li>
  	<li data-view="7">
         <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>             
 		</li>
  	<li data-view="4" class="active">
   		<a href="/3.mp3" singer="齐秦">往事随风</a>
  	</li>
  	<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
  	<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
  	<li data-view="5"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
	</ul>
</div>
'''

pattern='<li.*?active.*?singer="(.*?)">(.*?)></a>'
result=re.findall('singer="(.*?)">(.*?)</a>',context,re.S)
print(result)
print(type(result))   #<class 'list'>
for data in result:
    print(data)
    print(data[1])