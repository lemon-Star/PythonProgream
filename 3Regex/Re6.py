import re

#sub可以修改文本，比如想把一串字符的数字去掉，则可以使用sub
context='23sf232dfsdf32FFF3VVV23'
result=re.sub("\d+",'',context)  #replace()方法太繁琐   \d+ 匹配所有数字 替换成 ''
print(result)