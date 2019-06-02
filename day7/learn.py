
# #构建抽象类

# from abc import ABC, abstractmethod
# class BasePerson(ABC):
#     #普通方法，抽象方法，set, get, 
    
#     @abstractmethod
#     def say(self):
#         pass

# class Strdent(BasePerson):
#     def say(self):
#         print('我是学生')


# class Teacher(BasePerson):
   
#     def say(self):
#         for i in range(10):
#             print(i)

# s = Strdent()
# t = Teacher()
# def f(o):
#     o.say()
# # 多态--对不同类型发送相同的消息， 会有各自不同的操作
# f(s)
# f(t)


#----1-----
# from abc import ABC, abstractmethod
# #抽象类--不能直接用A创建对象
# class A(abc.ABC):
#     #普通实例方法
#     def f1(self):
#         print('普通的实例方法')

#     #抽象实例方法--必须在子类中重新实现
#     @abstractmethod
#     def f2(self):
#         print('实例方法')


# class B(A):
#     def f2(self):
#         print('B重写了分f2')

# b = B()
# b.f2()


# import Person   #导入person.py
# from Person import Person #导入person中的person类
# from Person import Person as P #设置别名P


# if __name__ == '__main__' #判断是否从当前入口执行的

# .表示当前路径
# ..表示当前路径的父目录


# #获取当前工作路径--通常配置成常量
# import os
# BASE_DIR = os.getcwd()
# path = os.getcwd()
# print(path)
#修改工作路径,路径拼接 windows->\\  linux->/
# os.chdir('BASE_DIR + '\\a')#参数--修改的工作路径
#对路径拼接
# p = os.path.join(BASE_DIR, 'a')
# # 分割为 路径 + 文件名
# print(os.path.split(path))
# #分割出 盘符
# print(os.path.splitdrive(path))
# #分割出 扩展名
# print(os.path.splittext(path))
# #判断指定的路径是否是文件
# print(os.path.isfile('./4.py'))
# #判断指定的路径是否是文件夹
# print(os.path.isdir('./5.py'))
# #判断指定的路径是否是绝对路径
# print(os.path.isabs(BASE_DIR))
# #判断指定路径是否存在
# print(os.path.exists('./xyz'))
# # print(p)
# # 判断文件的大小 单位是B字节
# print(os.path.getsize('./6pm.py'))
# #
# ct = os.path.getctime('./6pm.py') # 创建时间
# at = os.path.getatime('./6pm.py') # 访问时间
# mt = os.path.getmtime('./6pm.py') # 最近文件修改时间
# import time
# st = time.localtime(ct)
# print(st, time.strftime('%Y-%m-%d %H-%M-%S', st))
# st = time.localtime(at)
# print(st, time.strftime('%Y-%m-%d %H-%M-%S', st))
# st = time.localtime(mt)
# print(st, time.strftime('%Y-%m-%d %H-%M-%S', st))

# #获取路径下所有文件
# os.listdir(BASE_DIR)
# for i in l:
#     print(f'文件或文件夹：{i}')

#make driectory 创建目录
# os.mkdir(os.path.join(BASE_DIR, 'z'))
# os.mkdir(os.path.join(BASE_DIR, 'x\\xx'))#若中间的某个路径不存，会报错
# os.makedirs(os.path.join(BASE_DIR, 'x\\xx')) #若中间的某路径不存在，会自动创建出来


#remove移除文件
# os.remove(os.path.join(BASE_DIR, 'x\\xx'))
#rmdir--删除文件夹（只能删除空目录）
# os.rmdir(os.path.join(BASE_DIR, 'a'))
#删除指定路径的空目录（只能删除空目录）
# os.removedirs()


#重命名目录b为修改前的目录 bb为修改后的目录
#修改文件和文件夹名字
# os.rename(os.path.join(b, 'bb'))
# os.rename('./1.py', './a.py')
#移动并重命名--（第一个目标路径不存在会报错， 第二个目标路径不存在会自动创建）
# os.rename('./1.py', './bb/a.py')
# os.renames('./1.py', './bb/a.py')

# p = Person('小明')


# 例子1--删除
# def remove_all(path):

#     if os.path.isfile(path):#判断是否为文件
#         os.remove(path)#移除文件
#     else:
#         l = os.listdir(path)#获取路径下所有文件
#         for name in l:
#             p = os.path.join(path, name)#字符串拼接
#             remove_all(p)
#         os.rmdir(path)
    
# remove_all('./a')


# 打开文件
# r 只读方式打开
# f = open('./day7/1.txt', 'r', encoding='utf-8')
# # 读取文件内容
# countent = f.read()
# print(countent)
# # 读取一行
# countent = f.readline()
# print(countent, end='')
# countent = f.readline()
# print(countent, end='')
# # 读取多行 将每行内容当作列表中的一个元素 
# countent = f.readlines()
# print(countent, end='')
# f.close()

# # 打开文件
# # 写操作
# # w 会清空之前的内容
# # a 不会清空之前的内容
# f = open('./day7/1.txt', 'a', encoding='utf-8')
# # 直接写入指定的 str 内容
# f.write('你好\nhello\n')
# # 写入多条内容
# f.writelines(['你好\n','hello\n','world\n'])
# f.close()

# # 打开文件
# # 可读可写
# # w+ 会清空之前的内容 不存在会创建
# # a+ 不会清空之前的内容 在末尾添加 不存在会创建
# # r+ 不会清空之前的内容 光标从起始除开始写 会覆盖 不存在会报错
# f = open('./day7/1.txt', 'a+', encoding='utf-8')
# f.seek(0, 0)    #设置光标位置
# print(f'光标位置{f.tell()}')
# print(f.read())
# f.write('新内容\n')
# f.close()

# with 处理文件  多线程  完成后关闭
# 解析 csv 文件

# class Person:

#     def __init__(self, num, name, age):
#         self.num = num
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'ID: {self.num}  姓名: {self.name}  年龄: {self.age}'
        
# with open('./day7/data.csv', 'r+', encoding='utf-8') as f:
#     l = f.readlines()[1:]
#     for i in l:
#         i = i[:-1]
#         row_l = i.split(',')
#         number = row_l[0]
#         name = row_l[1]
#         age = row_l[2]
#         print(Person(number, name, age))

# # 直接读取
# import csv
# with open('./day7/data.csv', 'r+', encoding='utf-8') as f:
#     r = list(csv.reader(f))[1:]
#     for i in r:
#         print(Person(*i))
# 写csv文件
# import csv
# with open('./day7/data.csv', 'a+', encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerow(['4', '小高', '12'])

# # 例子
# import os

# def ls():
#     l = os.listdir(os.getcwd())
#     for i in l:
   
# def main_loop():
#     while True:
#         content = input('请输入内容(输入exit退出): ')
#         if content == 'exit':
#             break
#         # 以下对用户输入进行处理
#         ''' 
#         ls - os.listdir
#         cd xxxx - chdir
#         cwd - current work directory
#         mv xx xxx - 移动 重命名文件
#         mkdir xxxx - 创建文件夹
#         rmdir xxxx - 删除文件夹
#         rm xxx - 删除文件
#         cat xxx - 将文件内容显示出来
#         touch xxx - 创建文件
#         '''
#         l = content.split(' ')
#         if l[0] == 'ls':
#             ls()
#         elif l[0] == 'cd':
#             if not os.path.isabs(l[1]):
#                 p = os.path.join(os.getcwd(), l[1])
#             os.chdir(p)
#         elif l[0] == 'cwd':
#             print(os.getcwd())
#         elif l[0] == 'mv':
#             os.renames(l[1], l[2])
#         elif l[0] == 'mkdir':
#             print(l[0])
#         elif l[0] == 'rmdir':
#             print(l[0])
#         elif l[0] == 'rm':
#             print(l[0])
#         elif l[0] == 'cat':
#             print(l[0])
#         elif l[0] == 'touch':
#             p = l[1]
#             f = open(p, 'w')
#             f.close()
#         else:
#             print(f'无效命令 {content }')

# if __name__ == '__main__':
#     main_loop()

