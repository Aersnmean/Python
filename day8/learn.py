
# import csv

# with open('./data.csv', 'a+', encoding='utf-8', newline='') as f:
#     w = csv.writer(f)
#     r = csv.reader(f)



# import os
# # 判断该类中是否有该属性
# r = hasattr(os, 'mkdir')
# print(r)

# # 函数 复制指定文件到目标路径
# def cp(src, t):
#     if os.path.isfile(src):
#         with open(src, 'rb') as f1:
#             with open(t, 'wb') as f2:
#                 f2.write(f1.read())
#     else:
#         if not os.path.exists(t):
#             os.mkdir(t)
#         l = os.listdir(src)
#         for name in l:
#             cp(os.path.join(src, name), os.path.join(t, name))
# cp('./day8/a', './day8/b')



# 定义一个 Rect类, 属性长度length 和宽度width, 方法返回周长和面积
# 定义一个 Pos类, 属性 x 和 y 表示二维位置, rect 内有自己的坐标, 方法计算两个点之间的直线距离
# 扩展 rect, 计算指定的 pos 是否在 rect 范围内

# class Rect:
#     @property
#     def length(self):
#         return self.__length
#     @property
#     def width(self):
#         return self.__width
#     @property
#     def pos(self):
#         return self.__pos
#     def __init__(self, length, width, pos):
#         self.__length = length
#         self.__width = width
#         self.__pos = pos
#     def c(self):
#         return (self.__length + self.__width) * 2
#     def s(self):
#         return self.__length * self.__width
#     def is_in_rect(self, pos):
#         flag1 = self.pos.x <= pos.x and pos.x <= self.pos.x + self.width
#         flag2 = self.pos.y <= pos.y and pos.y <= self.pos.y + self.length
#         if flag1 and flag2:
#             return True
#         return False

# class Pos:
#     @property
#     def x(self):
#         return self.__x
#     @property
#     def y(self):
#         return self.__y
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#     def __sub__(self, other):
#         l = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
#         return l

# i = Rect(5, 6, Pos(0, 0))
# print(i.s(), i.c())
# a = Pos(0, -3)
# b = Pos(4, 0)
# print(b - a)
# print(i.is_in_rect(a))



# 单例 只能有一个实例对象
# class PersonManager:
#     __instance = None
#     __did_init = False
#     @staticmethod
#     def get_instance():
#         return PersonManager('小白')

#     def __init__(self, name):
#         if not PersonManager.__did_init:
#             self.name = name
#             PersonManager.__did_init = True
    
#     def __new__(cls, *args, **kwargs):
#         if not PersonManager.__instance:
#             PersonManager.__instance = super().__new__(cls)
#         return PersonManager.__instance

# pm1 = PersonManager('小白')
# pm2 = PersonManager.get_instance()
# print(pm1.name, pm2.name)


# # 进度条
# import time
# import os
# os.system('cls')
# for i in range(101):
#     print(f"'\r{'|'*i}{i}%'", end='')
#     time.sleep(1/24)



# try:
#     num = int(input('整数:'))
#     print(10 / num)
# except ValueError as err:
#     print('输入有误')
#     print(err)
# except ZeroDivisionError as err:
#     print('分母不能为零')
#     print(err)
# else:
#     # 没有发生任何异常
#     print('else')
# finally:
#     # 任何情况下均会执行
#     print('finally')



# class Person:
#     def __init__(self, name):
#         self.name = name
#         if '王吧' in self.name:
#             raise PersonNameError(self.name, '包含敏感词')

# # 自定义异常
# class PersonError(Exception):
#     pass

# class PersonNameError(PersonError):
#     def __init__(self, name, message):
#         self.name = name
#         self.message = message
#     def __str__(self):
#         return f'Person 的 name 出错: {self.name} {self.message}'

# try:
#     p = Person('黑王吧')
# except PersonNameError as err:
#     p = Person('黑**')
#     print(err.args)
#     print(err)
# else:
#     pass
# finally:
#     print(p.name)

