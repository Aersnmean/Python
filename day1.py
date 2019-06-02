count = 2
a = 0
b = 0
while a <= count:
    num = int(input(f'请输入第{a+1}个数'))
    a += 1
    if num > b:
        b = num
print(b)


print("hello world!!")
# 变量无类型说明
# 无常量 首字母大写（默认）
# int float str bool 
# 浮点数与小数的区别？
_a = 4
_a = 8
arge = 5.0
#能使用单引号尽量使用单引号  字符串中有单引号  字符转中有双引号
arge = "hello"
arge = 'hello'
PI = 3.14
print(_a)
#type（） 用来查看变量类型
print(type(_a))
# + - / *  操作数——运算符两边的数
# // 整除（取整）% 取余 ** 指数运算 
# [**] > [* / // % ] > [+ -] > [= += -= *= /= %=] > [and or not] > [=]
b = 5 % 2.5
b = 3 ** 5
b = 3 ** 0.5   
print(b)
#print后不能加空格
#print (type(b))
print(type(b))
arge = 1 / 1
print(arge)
print(type(arge))
a = 5
a = a + 2
a += 2
a -= 2
a *= 2
a /= 
a *= 2 + 1 # 相当于 a = a * (2 + 1)
 
a = 1 
b = 2
a = b = 3 # 不要这样写
# print(a,b)
# 字符串拼接
s = 'hi' + 'haha'  #结果 'hihaha'
s = 'hi' + 8    # 不可以
s = 'hi' * 3    #"hihihi"

a = 5 
b = "123456"
c = 2.2
print (a, b, c，sep='-') #5 123456 2.2 中间空格隔开 
#sep='-'——设置两个输出的中间的间隔符
#参数赋值不加空格
print(1, end='')# 不调到下一行   end = "*\n" 结束符——这行打印完后打印*在换行
print(2) #这两行打印在同一行 end = ""  print()默认换行 
print("\\") #打印单引号 \'打印单引号 \"打印双引号 \\ 打印反斜杠 \t 打印tab
#控制台获取 用户输入信息
r = input()  #是一个字符串类型  
r = input("请输入用户姓名：") 
age = input("请输入age:")
print(80 - age) # 80是int age是str  类型不同不能计算
# 需要 print(80 - int(age))
# int() float() str() 类型转换
print(r)


# a = 0.56
# 56%
# print(f'{a:20.2f}') # 冒号后面为约束条件 .2 小数点后两位  f——fload 20——整数和小数的位数和见面加空格
# print(f'{a:.0%}') # f——格式化字符串

# 以百分号形式显示
# print(str(a * 100 // 1) + '%') 


# a = 123456
# print(a % 10) #取个位上的数值
# print(a % 100 // 10) # 取十位上的数值

# a = 123456
# a_str = str(a)
# print(a_str[-1]) #打印 6
# print(a_str[2]) #打印 3

# b = input('你想获取哪个位数的值：')
# print(a_str[b])

# a = input('请输入一个数值：')
# print('你想获得这个数值的哪个位数:')
# print('个位数输入1', '十位输入2', '……',sep='，')
# b = int(input('请输入：'))
# print(a[-b])


#年份是闰年还是平年
# years = int(input('请输入一个年份：'))
# if years % 400 == 0 or (years % 4 == 0 and years % 100 != 0):
#     print('您输入的年份是闰年！')
# else:
#     print('您输入的年份是平年！')


# b = True
# c = 0 
# if b:
#     c = 1
# else:
#     c = 12
# c = 1 if b else 12  # if 的简写形式  

#输出路径
# path = r'C:\Desktop\nbc.tex'  # 路径  原始字符串前加r 
# path = '''C:\Desktop\nbc.tex''' # 加三个单引号 1输出字符串 2打印多行字符串  3多行注释
# print(path)

#截取字符串
a = 'abcdefgabdahbdabdabdabd'

# print(a[0:3]) # 打印abc 
#[start:end:step]
# print(a[0:5:2])  #每两个截一次 = 隔一个截一次 打印ace 
# print(a[0:-1]) #打印abcdef
# print(a[-3:]) #打印efg
l = len(a)
c = a.count('f') #反回子字符串 sub 在 [start, end] 范围内非重叠出现的次数

print(a.capitalize()) #返回原字符串的副本，其首个字符大写，其余为小写
print(a.find('de')) #查找指定字符串首次在字符串中的位置 如果未找到则返回-1
print(l)

#替换原字符串中的子字符串
b = a.replace('da','ji')
print(b)

#'da' 是否出现在字符串a 中   出现了 为 True  否则为  Fload
print('da' in a)


import random #随机生成数字
# i = random.randint(0, 9) #返回随机整数 N 满足 a <= N <= b。相当于 randrange(a, b+1)。
# i = random.randrange(0, 10)
# print(i)

# 且 或 非 and or not 逻辑运算符
# < > <= >= != == 
target = random.randint(0, 9)
number = int(input('请输入你猜的数字：'))
print('你的输入的数字是', number, '正确结果是', target)
# print(f'你猜的数字是：{number}  正确结果是：{target}')
s = 100
s -= abs(target = number) * 10

if s == 100 ：
    print('满分gg')
elif s >= 90：
    print('s')
elif s >= 80：
    print("a")
else:
    print('b')
    print('hello')
# if target == number:
#     print('猜对了！')
# elif abs(number - target) <= 2:
#     print('马上就要猜对了') 
# else:
#     print('猜错了！')


# 死循环
# while True:
#     pass

# a = 0
# while a < 5:
#     print('hello' + str(a))
#     a += 1


#do-while
#break
# count = 2
# i = 0
# while True:
#     print('这是第',i,'次')
#     i += 1
#     if i >= count:
#         break
# print(i)

#cotinue
# i = 0
# while i < 10:
#     i +=1
#     if i == 3:
#         continue
#     print(i)

#for-in循环
# s = 'adfjasdfjsd'
# for i in range(0,10)(::-1): #使字符串有下标
    # print(f'元素{i}')
    # print(s[i])
# for i in range(9,-1,-1):#打印9876543210
#     print(i)





