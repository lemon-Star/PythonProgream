import re

#利用compile可以创建一个正则对象，不用写多个
content1='2018-12-21 23:12'
content2='2019-10-11 15:30'
content3='2020-09-24 20:19'
pattern=re.compile('\d{2}:\d{2}')
result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result3=re.sub(pattern,'',content3)
print(result1)
print(result2)
print(result3)