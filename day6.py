#生成器--不保存元素，保存计算的算法， 可以放无穷个数
# t = (i for i in range(10))


#生成器函数--yield
# def f():
#     print('A')
#     yield 1   #1、返回结果 作用相当于return  2、next函数调用生成器时，执行到yield暂停，下次next继续执行
#     print('B')
#     print('c')
#     yield 2
#     print('D')
#g 是一个生成器
# g = f() #并不执行函数体 而是使g变成生成器
# for i in g:
    # print(f'i = {i}')
            # '''打印的结果
            # A
            # i = 1
            # B
            # c
            # i = 2
            # D
            # '''



# for i in t:
#     print(i)


#生成器
# t = (i for i in range(10))
# l = list(t)#只能使用一次
# print(l)
# print(list(t))#t是没有内容的



#递归函数--函数体内调用自己本身


# #面向对象--PersonManager是类（抽象概念）  p是类的对象（实例） -类的实例化-用类创建对象的过程
# class Person:    #大驼峰命名法
#     #静态特性name, age
#     #实例变量 或 成员变量 只能通过实例调用
#     def __init__(self, name, age):#self指代类创建的对象
        
#         self.name = name
#         self.age = age
#     #动态特性run, eat, sleep
#     #实例方法 方法
#     def info(self):
#         print(f'姓名：{self.name} 年龄：{self.age}')
    
# p = Person('老王', 23)
# p.info()




# class Goods:
    
#     #setter getter  变量变成属性
#     # 只读属性 不设置 setter
#     #gatter获取某个变量的值，该操作前后可以增加额外操作
#     @property
#     def name(self):#外界可以获取name
#         return self.__name

#     #setter设置（修改）变量的值，该操作前后可以增加额外操作
#     @name.setter
#     def name(self, value):
#         self.__name = value
        

#     def __init__(self, name, price, count):
#         #私有变量__name
#         self.__name = name  
#         #公共变量
#         self.price = price
#         self.count = count
#     def __str__(self):  #能使print（p）打印
#         return f'{self.__name}, {self.price}/个, {self.price}'


# p = Goods('可乐', 2, 23)
# # i = p.name
# p.name = '可口可乐'
# # print(i)
# print(p)



# class Person:
#     #类变量--修改时用 类名.类变量
#     age = 18

#     #静态方法--普通函数 --
#     @staticmethod
#     def f():
#         p = Person()
#         p.age = 18
#         return p


#     # #类方法--通过类名调用  不可使用成员变量和成员方法也就是不能使用self
#     # @classmethod
#     # def f(cls, a):#cls 不需要手动传值
#     #     print('类方法', a)

#     #实例方法
#     def __init__(self, name, ):
#         self.name = name
#     def __str_(self):
#         return f'姓名：{self.name}'

# p = Person('老王')
# Person.f(18)
# p.f()


# p = Person('老王')
# #类名调用类方法
# Person.f(18)
# #实例对象掉调用类方法
# p.f(34)

# p = Person('老王')
# #通过实例对象调用类变量
# print(p.age)
# p.ate = 100
# print(p.age)
# #通过类名使用类变量
# print(Person.age)
# Person.age
# print(Person.age)




# #继承
# class Person:

#     def __init__(self, name):
#         self.name = name
    
# class Student(Person):
#     pass
# s = Student()
# print(s)





# class Goods:
    
#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def count(self):
#         return self.__count


#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, v):
#         if v > 0：
#             self.price = v
#         else:
#             self.price = 0

#     def __str__(self):
#         return (f'商品：{self.__name} 价格：{self.__price} 数量：{self.__count}')
        

#     def __init__(self, name, price, count):
#         self.__name = name
#         self.price = price
#         self.__count = count

#     def sell(self, i):
#         sell_count = i
#         if self.__count < i:
#             sell_count = self.__count
#         self.__count -= sell_count
#         m = sell_count * self.__price
#         return m


#     def add(self, i):
#         if type(i) is int and i > 0:
#             self.__count += i
#         return self.count

# g1 = Goods('可乐', 2.5, 12)
# g2 = Goods('雪碧', 3, 2)
# l = [g1, g2]



#多继承
# class A:
#     def say(self):
#         print('hi')
# class B(a):
#     #先调用父类初始化方法
#     super().say()
#     print('B say')



# #枚举
# from enum import Enum, unique
# #是可迭代的

# @unique
# class States(Enum):
#     Main = 0
#     Login = 1
#     Register = 2
#     RestPassword = 3
#     Buy = 4

# current_state = States.Main
# print(current_state)
# print(States.Main)



# def geratest_common_divisor(a,b):
#     if a < b:
#         a, b = b, a
#     else:
#         while a - b != 0:
#             r = a % b
#             a = b
#             b = r
#     return b

# def multile(a, b):
#     i = geratest_common_divisor(a,b)
#     grent = a * b / i
#     return grent

# class Fraction:
#     def __init__(self,numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
        
#     def __add__(self, other):
        
#         if other.denominator == self.denominator:
#             mild = self.numerator + other.numerator
#             return Fraction(mild, other.denominator)
#         else:
#             b = multile(other.denominator, self.denominator)
#             a = b / self.denominator
#             self.numerator *= a
#             other.numerator *= a
#             mild = self.numerator + other.numerator
#             return Fraction(mild, b)

#     def __sub__(self, other):
#         if self.denominator == other.denominator:
#             mild = self.numerator - other.numerator
#             return Fraction(mild, other.denominator)
#         else:
#             b = multile(other.denominator, self.denominator)
#             a = b / self.denominator
#             self.numerator *= a
#             other.numerator *= a
#             mild = self.numerator - other.numerator
#             return Fraction(mild, b)
    
#     def __mul__(self, other):
#         numerator = self.numerator * other.numerator
#         denominator == self.denominator * other.denominator
#         # a = geratest_common_divisor(numerator, denominator)
#         # numerator = numerator / a
#         # denominator = denominator / a
#         return Fraction(numerator, denominator)

#     def __truediv__(self, other):
#         numerator = self.numerator * other.denominator
#         denominator = self.denominator * other.numerator
#         # a = geratest_common_divisor(numerator, denominator)
#         # numerator = numerator / a
#         # denominator = denominator / a
#         return Fraction(numerator, denominator)




#     def __str__(self):
#         if self.numerator == self.denominator:
#             return '1'
#         else: 
#             a = geratest_common_divisor(self.numerator, self.denominator)
#             self.numerator /= a
#             self.denominator /= a
#             return f'{self.numerator} / {self.denominator}'




# f = Fraction(5, 6)
# g = Fraction(1, 6)

# print(f + g)
# print(f * g)
# print(f / g)
# print(f - g)










