import re

#group(1) 会输出第一个贝 （） 括号包起来的匹配上的数据
content='Hello 1234556 World_This is a Regex DeMon'
print(len(content))
result=re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
