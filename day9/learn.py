
# import json

# l = [1, 2, 3, 4]
# d = dict(a=1, b=2, c=3)
# t = (1, 2, 3, 4)

# json_str = json.dumps(t)
# print(type(json_str), json_str)

# # 序列化
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, num):
#         super().__init__(name, age)
#         self.num = num

# p1 = Person('小白', 19)
# p2 = Student('小黑', 18, 45)
# l = [p1, p2]
# d = {'count': 2, 'data': l}

# def f(p):
#     return dict(name=p.name, age=p.age)
# def fp(p):
#     # if type(p) is Person:
#     #     print('Person', type(p))
#     # elif type(p) is Student:
#     #     print('Student', type(p))
#     # isinstance 判断父类为True
#     if isinstance(p, Person):
#         return dict(name=p.name, age=p.age)
#     elif isinstance(p, Student):
#         return dict(name=p.name, age=p.age, num=p.num)

# json_str = json.dumps(d, default=fp, indent=4)
# print(json_str)

# json_str = '''
# {
#     "count": 2,
#     "data": [
#         {
#             "name": "\u5c0f\u767d",
#             "age": 19
#         },
#         {
#             "name": "\u5c0f\u9ed1",
#             "age": 18
#             "num": 45
#         }
#     ]
# }
# '''

# def f(d):
    

# data_dic = json.loads(json_str, object_hook=f)
# print(data_dic)

# # json str -> object
# # object_hook=func(dict)
# json.loads()
# # json 文本 -> object
# json.load()
# # object -> json str
# # default=func(obj)
# # indent=4  缩进
# json.dumps()
# # object -> json 文本
# json.dump()


# import json
# from urllib import request, parse

# # GET POST
# citys_url = 'http://v.juhe.cn/weather/citys'
# geo_url = 'http://v.juhe.cn/weather/geo'
# key = '106660492a187fc6c048e3b13de172a7'
# # 请求
# def my_request(url,method='get', **kwargs):
#     # 将参数字典编码成 url 中的参数格式
#     params_str = parse.urlencode(kwargs)
#     req = None
#     if method == 'post':
#         post_data = params_str.encod(encoding='utf-8')
#         # 创建请求
#         req = request.Request(url, data=post_data)
#     else:
#         req = request.Request(url + '?' + params_str)
#     # 发送请求并获取响应信息
#     res = request.urlopen(req)
#     # 读取响应的数据
#     res_data = res.read()
#     # 对数据解码
#     res_str = res_data.decode(encoding='utf-8')
#     # 返回数据字符串
#     return res_str

# cities = my_request(citys_url, key=key)
# with open('./day9/cities.json', 'w', encoding='utf-8', newline='') as f:
#     f.write(cities)
# print(cities)
    


from xml import sax
from xml.dom import minidom

xml_str = '''
<root>
    <count>3</count>
    <data>
        <item id="1">
            <name>可乐</name>
            <price>2.5</price>
            <count>5</count>
        </item>
        <item id="2">
            <name>雪碧</name>
            <price>2.5</price>
            <count>13</count>
        </item>
        <item id="3">
            <name>康师傅</name>
            <price>5</price>
            <count>18</count>
        </item>
    </data>
</root>
'''

doc = minidom.parseString(xml_str)
# 获取所有的 item 标签元素
items = doc.getElementsByTagName('item')
# 遍历所有的 item 标签元素
for i in items:
    # 一次获取每个item元素的 id 属性
    if i.getAttribute('id') == '2':
        for n in i.childNodes:
            if n.childNodes:
                # 标签中的文本也是一个节点
                print(n.childNodes[0].data)


# class MyXMLHandler(sax.ContentHandler):
#     def __init__(self):
#         self.current_e = ''
    
#     def startDocument(self):
#         pass
    
#     def endDocument(self):
#         pass
    
#     def startElement(self, name, attrs):
#         self.current_e = name
    
#     def endElement(self, name):
#         pass
    
#     def characters(self, content):
#         if self.current_e == 'name':
#             print(content)


# h = MyXMLHandler()
# # sax.parse()  解析 xml 文件或者 url
# sax.parseString(xml_str, h)
