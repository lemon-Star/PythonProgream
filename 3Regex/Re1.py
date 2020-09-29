import re

#match从开头就开始匹配，匹配不上就不往后走
content='Hello 123 4556 World_This is a Regex DeMon'
#content='111Hello 123 4556 World_This is a Regex DeMon'
print(len(content))
result=re.match('^Hello',content)
print(result.group())
print(result.span())
