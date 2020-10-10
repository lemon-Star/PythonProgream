import json

data= [
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

#还可以通过 dumps（）方法将JSON对象转化成字符串，然后再调用文件存储write（）方法写入文本
#还可以通过 dumps（）方法将JSON对象转化成字符串，然后再调用文件存储write（）方法写入文本
print(type(data))
str=json.dumps(data)
print(type(str))
print(str)
with open('JSONData3.json','w') as file:
    file.write(str)

#如果想保存成JSON格式，加入一个参数indent，代表缩进字符个数
with open('JSONData31.json','w')as file:
    file.write(json.dumps(data,indent=2))

#包含中文，则保存会乱码，需要重新编码
data2=[
    {
        "name":"爱新觉罗",
        "age":"24",
        "address":"北京紫禁城中宫"
    }
]
with open("JSONData32.json",'w') as file3:
    file3.write(json.dumps(data2))
#上面会乱码 unicode编码格式，需要定义编码格式
with open("JSONData33.json",'w',encoding='UTF-8') as file4:
    file4.write(json.dumps(data2,indent=2,ensure_ascii=False))