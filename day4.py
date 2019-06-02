    #dict-字典
# d = dict()  #空字符串
# d = dict(a = 1, b = 2)

# d = {'name': '老王', 'age': 18, 3: 'hello'}    #{'key': 'value'}-value can any type .key often str
# #key can't use list but can tuple

# print(d[3])    #通过key找value

# i = d['a']    #把a的值赋值给i

# d.update(d = 4) #追加元素 和 更新已有的元素 可同时更新多个元素

# d['c'] = 3  #追加元素 和 更新已有的元素

# i = d.pop('a', -1)  #通过key删除元素 i为a的值 ，if key 不存在 则返回 -1

# d.clear()   #清空d

# d['a']  #查找a的值

# j = d.get('a', -1) #把a的值付值给j，如果a不存在，则返回-1

# j = d.setdefault('xxx')   #把a的值付值给j，
#                           #如果a不存在，则返回-1,如果不填则返回none,而且还会在d中增加一个key：value

# print(j)
# print(d)

# if 'a' in d:  #判断key是否在d中

#     print('yes')
# print(len(d))   #d 的长度

# for k in d: 遍历d
#     print(k, d[k]) #输出key 和 根据key输出value

# for v in d.values():  #根据value输出value
#     print(v)

# l = list(d.values)  #把value放在列表l中
# i = list(d.keys)    #把key放在列表l中
# g = list(d)         #把key放在列表l中


# for k, v in d.items():    #同时获取key value
#     print(k, v)

#推导式
# d_new = {k: v * 2 for k, v in d.items()}
# d_new = {k: d[k] * 2 for k in d}
# print(d_new)

    
# def f(name: str): #函数头 说明name为str类型
#     print('hello')
# f()



# def week_with_date(year, mouth, day):
#     w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
#     return w

# i = input('请输入日期（yyyy-mm-dd）:')
# s = i.split('-')
# y, m, d = int(s[0]), int(s[1]), int(s[2])
# mm = 13 if m == 1 else (14 if m == 2 else m)
# a = week_with_date(y, mm, d)
# print(a)


# def func(name: str):
#     print(name)
# func(15)

# #''' ↓
# def date_str(year, mouth):
#     m31 = [1, 3, 5, 7, 8, 10, 12]
#     m30 = [4, 6, 9, 11]
#     d = 31 if mouth in m31 else (30 if mouth in m30)
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         d = 29
#     else:
#         d = 28
#     return d

# i = input('请输入年月（yyyy-mm):')
# s = i.split('-')
# y, m = int(s[0]), int(s[1])
# day = date_str(y, m)
# print(day)
# #''' ↑

# age = 18
# def change_age(age_new):
#     global age  #global声明之后 就可以修改全局变量
#     age = age_new
# change_age(22)
# print(age)
 
# #↓
# def get_data():
#     i = input('请输入年份和月份（yyyy-mm）:')
#     s = i.split('-')
#     y, m = int(s[0]), int(s[1])
#     return y, m, 8, 0, 8, 9 #可同时返回多个指，相当于一个元组，省略了小括弧

# a = get_data()
# print(a)
# #↑

# def f(a, b):
#     a, b = b, a
#     return a, b
# x, y = 5, 10
# x, y = f (x, y)
# print(x, y)


# def f (l: list)：
#     l.append(88)
# L = [1, 2, 3]
# f(L)
# print(L)


# def f(a, b, c=1):  #默认值赋值必须从最后一个参数开始默认赋值
#     print(a, b, c)
# f(1, d = 2, c = 3)  #关键词赋值之后，后面都必须使用关键词赋值
# f(4, 9)


# print('hi', 'hello')

#定义可变参数
# def f(*args): #args为一个元组
#     print(args)
# f(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# def sum_int(*args):
#     r = sum(args)   #sum 后为一个 可迭代的元素
#     return r
# a = sum_int(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(a)



# def f(**kwargs):    #可变关键词参数
#     print(kwargs)   #输出为一个字典
# f(a = 1, b = 2) #有关键字，有值


# def f(**kwargs):
#     for k, v in kwargs.items:
#         print(f'k：v')
# f(name = '89', nianling = 'da', sdc = 'fd')

#args 前只能用顺序赋值
#args 后只能用关键词赋值
#args 只能用顺序赋值
# def f (a, b, *args, c, d):
#     print(a, b, c, d, args)
# f(1, 2, 3, 4, 5, 6, 7)


#顺序只能是先args(顺序赋值)后kwargs（关键词赋值）
# def f(*args, **kwargs):
#     print(arfs, keargs)
# f(1, 2, 3, 4, 5, 6, a = 1, b = 2)


# def f(a, b, c, *args, d = 0, **kwargs):
#     print(a, b, c, d ,args, kwargs)   #1 2 3 0 (4, 5, 6) {'x': 1, 'y': 2, 'z': 3}
# f(1, 2, 3, 4, 5, 6, x = 1, y = 2, z = 3)

# t = (1,)
# print(t)


#集合 --无序  元素不可重复 集合运算
# s = set()
# s = {2, 3, 4, 6, 7, 8, 9,}
# s1 = {2, 3}

# s1 = s1 & s2
# s1 &= s2 (|= ^= -=)

#只包含在s不包含在s1中的集合
# print(s - s1)

#两个集合的交集的补集
# print(s1 ^ s)

#两个集合的交集
# print(s1 & s)

#两个集合的并集
# print(s1 | s)

#检测每个元素是否都在另一个集合中,两个集合不可以相等
# print(s1 < s)

#检测每个元素是否都在另一个集合中,两个集合可以相等
# print(s1 <= s)

#增加元素值
# s.add(-1)

#删除元素值
# s.remove(9)

#随机删除元素
# a = s.pop()
# print(a)

#添加元素-必须数可迭代元素
# s.update([1, 2, 3, 4])

# if 4 in s:

# print(len(s))


# print(s)
# print(type(s), s)   #<class 'set'> set()



# def draw_line():
#     print('*' * 20)
# draw_line()

# def draw_line():
#     print('*' * 20)
#     print('*' * 5, 'Wecome', '*' * 5)
#     print('*' * 20)
# draw_line()

# def get_sum():
#     sum = 0
#     for i in range(10):
#         sum += i
#     print(sum)
# get_sum()

# def get_sum(start, end):
#     sum = 0
#     for i in range(start, end):
#         sum += i
#     print(sum)
# get_sum(5, 10)

# def ave(*args):
#     sum = 0
#     for i in range(len(args)):
#         sum += arge[i]
#     a = sum / len(args)
    
# a = ave(6, 4, 5, 9)
# print(a)

# def filter(*args):
#     l = []
#     for i in args:
#         if type(i) is int:
#             l.append(i)
#     return l
# l = filter('x', 4, 8, 'k')
# print(l)

# def max_int(*args):
#     a = args[0]
#     for i in args:
#         if a < i:
#             a = i
#     a = i if a < i
#     return a
# print(max_int(3, 4, 7, 34, 6, 76))

# def func(a, b):
#     '''随便写的额'''
#     print(a, b)
# # s = func.__doc__ #注释
# s = func
# s(1, 2)
# # print(s)


    #函数嵌套
# def f():
#     print('f')
#     def f1():
#         print('f1')
#     return f1
#
# my = f()
# my()


