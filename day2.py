
# num = int(input('你想要几个*呀？：'))
# a = 0
# # while a <= num:
# #     print('*' * a)
# #     a += 1
# for a in range(num):
#     print('*' * (a + 1))
          #num k
#     *      0 4
#    ***     1 3
#   *****    2 2
#  *******   3 1
# *********  4 0
#  *******   5 1
#   *****    6 2
#    ***     7 3
#     *      8 4
# num = int(input('你想要几行*啊：'))
# a = 0
# if num % 2 != 0:
#     b = num // 2 + 1
#     for a in range(b):
#         print(' ' * (b - a) + '*' * (a * 2 + 1))
#     for a in range(b,num+1):
#         print((' ') * (a - 3) + '*' * ((num - 1 - a) * 2 + 1))

# for i in range(n)
# mid = n // 2
# star_count = 0
# space_count = 0
# if i <= mid:
#     star_count = i * 2 +1

#前十个数相加
# n = 10
# sum = 0
# for a in range(1,n+1):
#     sum = sun + a
# print(sum)

#计算最大公约数

# a = int(input('亲请输入第一个数：'))
# b = int(input('亲请输入第二个数：'))
# if b > a:
#     a , b = b , a
# # a = 500
# # b = 100
# r = a % b
# while r != 0:
#     a = b
#     b = r 
#     r= a % b
#     # a , b, r= b , r ,b-r
# print(f'最大公约数{b}')


# #列表
# l = [1, 'i', 'r', 'er', True]
# l.append('hello') #末尾增加元素
# l.insert(4,'imp')#插入元素到指定下标位置
# l.extend([])#把一个可迭代的类型一个一个追加到列表后面
# l.pop(3) #删除元素 删除第三个元素 如果不写3 默认删除最后一个 列表不能为空
# l.remove('i') #删除元素值 
# l[1:2] = [5, 6] #切片替换 把第二个元素替换为后者
# l[3] = 2 #修改元素的值（通过下标查找）
# b = l[3:4]#截取l的子列表
# l.reverse#反转列表l
# b = l[::-1]#反转列表l 给b
# print(max(l))#列表最大值 min最小值
# l.index()#指定元素值出现的位置
# b = l.count('hello') #字符出现的次数
# print(l)
# print(b)


# l = list(range(10)) 
# # l = [1, 2, 3, 5, 6]
# for i in range(len(l)):
#     l[i] = i * 2
# print(l,end='')

# a = 3
# b = 4
# a = 12
# print(id(a)) #查看在内存的位置
# print(id(b))
# if a == b:
#     print('相等')

# a = [1, 2, 3, 4,]
# # b = a  # 修改a后b也发生变化
# # a[0] = 'a'
# # print(id(a))    #查看在内存的位置
# # print(id(b))
# # a.clear()   #a还是列表清空列表
# # del a   #a还是列表清空列表
# # a = None    #l不是一个列表了
# b = a[::] 
# b[0] = 'e'
# print(b) 
# print(a)

# month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# num = int(input('请输入月份'))
# print(month[6-1])


# #列表转字符串
# l = ['1', '2', '3', '4', '5']
# s = ''
# s = s.join(l)   #s = ''.join(l)  作用一样 列表转字符串
# print(s)
# print(str(l))   #列表转字符串

# #字符串转列表
# s = '12,345,67,8'
# l = s.split(',')    #以逗号为分隔符转换为列表
# print(list(l))  #字符串转列表


# for i in range(3):
#     for j in range(2):
#         print(f'i = {i}, j = {j}')

#九九乘法表
# for i in range(1, 10):
#     for j in range(i, 10):
#         sum = i * j
#         print(f'{i} * {j} = {sum}\t',end = '')
#     print()

# l = [1, 2, 4, 3, 5]
# for i in range(len(l))
#     if i == 2:
#         l.pop(i)    #删除下表为i的元素
    


import random
l = []
# for循环不行
# for a in range(5):
#     i = random.randint(1, 9)
#     b = l.count(i)
#     if b == 0:
#         l.append(i)
#     else:
#         a = a - 1


#随机数放在列表里
# while len(l) < 5:
#     i = random.randint(1, 9)
#     b = l.count(i)
#     if b == 0:
#         l.append(i)
# print(l)

#冒泡排序
# i = len(l)

# while i != 1:
#     for j in range(0, i-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
#         print(l)
#     i = i - 1

#水仙花数
# for a in range(100, 1000):
#     i = a // 100
#     j = a % 100
#     c = j // 10
#     h = j % 10
#     b = i ** 3 + c ** 3 + h ** 3
#     if a == b:
#         print(f'{a} 是水仙花数')


#最少张数
# money = [100, 50, 20, 10, 5, 1]
# b = int(input('请输入金额'))
# for a in money:
#     d = b // a
#     b = b % a
#     if d != 0:
#         print(f'{a}需要{d}张')


# m = 7
# l = []
# j = 1
# while j < m:
#     l.append(j)
#     j = j + 1

# i = 0
# while True:

#     print(l[i])
#     i = i + 1
#     if i == len(l):
#         i = 0



