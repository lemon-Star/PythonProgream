
with open('lxml1.txt','a',encoding='utf-8') as f:
    f.write('''对于网页节点来说，他可以定义id，class或其他属性，节点之间还有层次关系，在网页中可以通过
    Xpath或CSS选择器来定位一个或者多个节点。利用这些解析则提取数据会方便很多。 \n
    XPath全程XML Path Language，即XML路径语言   \n
    nodename:选择此节点的所有子节点  \n
    /  从当前节点选择直接子节点  \n
    // 从当前节点选择子孙节点   \n
    .  选取当前节点   \n
    .. 选取当前节点的父节点 \n
    @ 选取属性 \n
    ''')