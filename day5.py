# def f(*args):
#     for i in range(len(args)):
#         print(f'{i} -- {args[i]}')

# l = list(rang(4))
# f(*l)

# def fun(l):
#      for i, v in enumerate(l):#enumerate(可迭代对象)  同时取出下标i,和对应的值v
#          print(f'{i} -- {v}')
#
# fun(l)


# def f(a): #推迟函数执行的过程
#     print(type(a))
#     a('hello')
# f(print)


# l = [3, 5, 6, 8, 2, 1]
# def f(li, func):
#     l_new = []
#     j = func(i)
#     l_new = [j for i in li]
#     return l_new

# def f2(old_value):
#     return old_value * 2

# print(f(l))

# import time
# from time import sleep

# def timer(t, will_begin == None, did_end == None):
#     # will_begin()
#     if will_begin:
#         will_begin()
#     time.sleep(t)
#     # print('end')
#     if did_end:
#         did_end()
# def f2():
#    print('start')
# timer(2, f2)

# def f3():
#     for i in range(1, 11):
#         print(i)
# timer(5, f3)
# def f1():
#     print('nihao')
# timer(2, did_end = f1)


# def f(i, t, func, *args, **kwargs):
#     for i in range(i):
#         time.sleep(t)
#         func(*args, **kwargs)
# def f2(name, age):
#     print(name, age)
# f(2, 3, f2, 'laowang', '10')



# a = lamnda i: i * 2 #匿名函数函数，只能放在一行，必须有返回值
# r = list(map(lamb i: i * 2, 1))
# print(a)

# def sort_a(l, func):
#     pass

# def f(i, j):
#     return i > j

# sort_a(l, f)

# def f():
#     i = 0
#     print(id(i))
#     def f1():
#         nonlocal i
#         i = 5
#         print(id(i))
#     return f1
# a = f()
# a()

# import functools
# functools.wraps 
# #装饰器函数 语法糖 包装fun函数
# def f(func):
#     @functools.wraps(func)#控制包装器
#     def f1(): #包装器
#         print('start')
#         func()
#         print('end')
#     return f1

# @f#调用 装饰器 语法糖  函数功能不会变，会在执行时 前后加装饰
# def my():
#     print('my')
# my() #输出 start my end 之后调用my()时 

# @f
# def hi():
#     print('hello')
# hi()




# def log(count):
#     def _log(func):
#         @functools.wraps(func)
#         def log1(*args, **kwargs):
#             n = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             print(f'[{n} {func.__name__}] {count}')
#             i = func(*args, **kwargs)
#             return i
#         return log1
#     return _log

# @log('imp最棒')
# def f(b):
#     print(f'hello,{b}')
# f('imp')

# #装饰器
# def timer(func):
#     #包装器
#     @functools.wraps(func)
#     def f1():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         delter_ = (t2 - t1) * 1000
#         print(f'{delter_:.4f} ms')
#     return f1

# @timer
# def f():
#     l = []
#     for i in range(10000):
#         for j in range(100000):
#             l.append(i * j)
#     return l
# f()

# t1 = time.time()
# f()
# t2 = time.time()
# delta_t = t2 - t1
# print(f'{delta_t:.4f} ms')


#装饰器
# def f(a, b)
#     def _f(func):
#         #包装器
#         @functools.wraps(func)
#         def warr(*args, **kwargs): #warr称为闭包执行闭包所依赖的context
#             print(a)
#             i = func(*args, **kwargs)
            
#             print(b)
#             return i
#         return warr
#     return _f

#练习3
# @f('1', '2')
# def f1(count):
#     l = list(range(count))
#     return l
# l = f1(10)
# print(l)


#练习2
# @f
# def say_hi(name):
#     print(f'Hello,{name}')
# say_hi('小明')

#练习1
#语法糖---装饰器
# @f
# def f1():
#     print('nihao')
# f1()

