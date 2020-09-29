import re

#match是从开头开始匹配，一旦开头不匹配，那么整个匹配就失败了  适合检测某个字符串是否满足这则表达式规则
#
#content='Hello 1234556 World_This is a Regex DeMon'
content='3232Hello 1234556 World_This is a Regex DeMon'
print(len(content))
result=re.search('Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
