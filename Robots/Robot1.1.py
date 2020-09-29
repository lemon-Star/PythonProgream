
fileName='/Users/star/PycharmProjects/pythonProject/Robots/robots.txt'
f=open(fileName,'w')
f.write("Use-agent:*\n"
        "Disallow:/\n"
        "Allow:/pulic/\n")
f.write("一般放在网站的根目录下，和网站的入口文件 index等 放在一起，\n"
        "user-agent描述了搜索爬虫的名称，* 则代表对任何爬虫有效 比如 user-agent：Baiduspider 只是对百度爬虫开放\n"
        "Disallow：指定了不允许抓取的目录，/则表示不允许抓取所有\n"
        "Allow：一般和Disallow一起使用，允许抓取的目录 /public 允许抓取/public下的所有\n")

f.close();
