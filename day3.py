#元组——元素内容不可变化 可以解包
# a = tuple()
# b = (1, 2, 4, 5, 2)
#  无该操作 append pop

#index——通过内容获取下标
# print(b.index(2))

# print(b.count(2))   #出现的次数

# if 1 in b:    #1是否在元组中
#     print('yes')

#拼接元组
# print(a + (5, 6, 7))

# t = tuple(range(4)) #快速赋值
# a, b, c, d = t  #解包
# a, b, *c = t    #部分解包c是一个元组
# a, *b, c = t    #部分解包c为最后一个元素b为中间的全部
# print(a, b, c)
# print(a, b, c, d)

#print(type(a),a)
# print(b[])
# print(len(b))#获取元组长度

    #列表中放列表
# L1 = list(range(3))
# L2 = list(range(6))
# L = [L1, L2]
# # print(L)
# for j in L:
#     for i in j:
#         print(i, end = '--', sep = '\\')
    

    #元组中放元组
# t1 = tuple(range(5))
# t2 = tuple(range(5, 12))
# t = (t1, t2)
# for i in t:
#     for j in i:
#         print(j, sep = '--')
# for i in range(len(t)):
#     for j in range(len(t[i])):
#         print(t[i][j], end = '--')

    #例子
# l = list(range(100))
# b = [] 
# for i in range(len(l)):
#     j = l[i] ** 2
#     b.append(j)
# print(b)

    #例子
# l = list(range(10))
# l_new = []
# for i in l:
#     if  i % 10 == 7 or i // 10 == 7 or i % 7 == 0:
#         l_new.append(i)
# print(l_new)


    #例子
# l_new = []
# j = 2
# for i in range(2, 100):
#     if j < i:
#         for j in i:
#             if i % j == 0:
#                 continue
#             else:
#                 l_new.append(i)
# print(l_new)


    #100内的质数
# l = []
# for i in range(2,100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else :
#         l.append(i)


# m = int(input('请输入一个数：'))
# for i in range(2, m-1):
#     while m != 1:
#         if m % i == 0:
#             print(i)
#         else:
#             break
#         m = m / i
        
        

# l = tuple(range(1000))
    #推导式
# l_new = [i ** 2 for i in l ]
# l_new = [i * 2 for i in l]
'''
[表达式(对可迭代对象进行的操作) for 变量 in 可迭代对象 if 条件]
[if 表达式 else 表达式]
'''
# l_new = [i // 2 for i in l]
# l_new = [i for i in l if i % 7 == 0 or i // 10 == 7 or i % 10 == 7]
# l_new = ['奇数' if i % 2 != 0 else '偶数' for i in l]
# l_new = [1 if 0 <= i <= 9 else 3 if 100 <= i <= 999 else 2 for i in l]
# l_new = [(x, y) for x in range(10) if x % 2 != 0 for y in range(10) if y % 2 == 0]
# print (l_new)

# import random
# l1 = [random.randint(0, 100) for i in range(20)]
# l2 = [random.randint(0, 100) for i in range(20)]
# l = [i for i in l1 if i in l2]
# print(l1)
# print(l2)
# print(l)

    #例子
# l = [0, 1]
# [l.append(l[i] + l[i+1]) for i in range(20)]
# print(l)


# w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
# y = int(input('请输入年份:'))
# m = int(input('请输入月份:'))
# d = int(input('请输入日期:'))
# i = input('请输入日期(yyyy-mm-dd):')
# s = i.split('-')#以-分割字符串
# y = int(i[0:4])
# m = int(i[5:7])
# d = int(i[8:11])
# if m == 1:
#     y -= 1
#     m = 13
# if m == 2:
#     y -= 1
#     m = 14
# w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
# print(f'这天是周{w}')


# l = [1, 2, 3]
# for i in l:
#     for j in l:
#         for h in l:
#             if i != j and i != h and j != h:
#                 print(i * 100 + j * 10 + h)
    
# l_new = [i * 100 + j * 10 + h for i in l for j in l for h in l if i != j and i != h and j != h]

# print(l_new)


# i = input('请输入年月(yyyy-mm)：')
# s = i.split('-')
# y = int(s[0])
# m = int(s[1])

# l = [1, 3, 5, 7, 8, 10, 12]
# g = [4, 6, 9, 11]


# if m in l:
#     dd = 31
#     # l = list[range(1, m + 1)]
# elif m in g:
#     dd = 30
#     # l = list[range(1, m + 1)]
# elif y % 400 == 0 or (y % 4 == 0 and y %100 != 0):
#     dd = 28
#     # l = list[range(1, m + 1)]
# else:
#     dd = 29
#     # l = list[range(1, m + 1)]
# print('一 二 三 四 五 六 日')
# print('-' * 20)
# d = 1
# w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
# # if w == 1:
# #     [print() if j % 8 == 0 else print(j, end = '    ') for j in range(1, m + 1) ]
# # print('     ' * (w - 1))
# # [print('     ' * (w - 1)) if j % 8 == 0 for j in range(1, d + 1)]

# print(' ' * (w - 1) * 3, end = '')
# i = 0
# for j in range(1, 8 - w + 1):
#     print(j, end = '  ')
# for k in range(8 - w + 1, dd + 1):
#     print(k, end = '  ')
# print('-' * 20)
#     # print()
#     # print(j,end = ' ')




