from urllib.robotparser import RobotFileParser

#Robotparse模块来解析Robots文件， 模块中提供了以RobotFileParse来判断
rp=RobotFileParser()
rp.set_url("http://www.jianshu.com/robots.txt")
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&age=1&type=collections'))