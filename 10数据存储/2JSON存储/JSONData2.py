import json

str='''
    [
    {"name":"Maker",
     "age":"14",
     "birthday":"2011-09-09"
    },
    {
     "name":"Bob",
     "age":"24",
     "birthday":"1992-08-08"
    }
    ]
'''
print(type(str))
data=json.loads(str)
print(data)
print(data[0])
print(data[0]['name'])
print(data[0]['age'])
print(data[0]['birthday'])
print(type(data))
#读取json文件的文本内容
with open('JSONData2.json','r') as file:
    ss = file.read()
    data=json.loads(ss)
    print(data)