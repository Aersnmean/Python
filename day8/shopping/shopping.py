
import functools
import datetime
import time
import os
import user
import good 

judg = 0
information = []
comment = [
    {'name': '雪糕', 'count': 4,  'pric': 4},
    {'name': '雪碧', 'count': 23,  'pric': 3},
    {'name': '冰露', 'count': 10,  'pric': 1},
    {'name': '怡宝', 'count': 43,  'pric': 2},
    {'name': '农夫山泉', 'count': 4,  'pric': 2},
    {'name': '百岁山', 'count': 43,  'pric': 4}
    ]
def index():
    os.system('cls')
    username = input('请输入用户名：')
    if not user.is_in_csv(username):
        password = input('请输入密码：')
        user.insert(username, password)
        print(f'恭喜{username}注册成功!!')
    else:
        print('该用户名已存在')
        index()
    time.sleep(1.3)
    os.system('cls')
    play()

def login():
    global judg
    os.system('cls')
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if user.login(username, password):
        print('登录成功')
        judg = 1
        other()
    else:
        print('用户名或密码错误')
        login()

def password():
    global information
    get_user = input('用户名：')
    get_oldpassword = input('旧密码：')
    for find in range(len(information)):
        if get_oldpassword == information[find]['password']:
            get_newpassword = input('新密码：')
            information[find] = get_newpassword
            print('密码修改成功啦！！')
        else:
            print('旧密码输入有误，请重新输入：')
            password()

def other():
    os.system('cls')
    j = 1
    for i in comment:
        print(f"{j}、{i['name']}, {i['count']}, {i['pric']}", sep = '   ')
        j += 1
    shopping = int(input('请输入要购买商品的标号：'))
    if judg :
        counts = int(input(f"请输入购买{comment[shopping - 1]['name']}的数量："))
        money = int(input(f"请付{counts * comment[shopping - 1]['pric']}元，谢谢！！:"))
        if money == counts * comment[shopping - 1]['pric']:
            reshopping = input('还要再来些吗？(Y/N)')
            if reshopping is Y or reshopping is y:
                other()
            else:
                print('慢走啊！！')
        else:
            print('您输入有误，请重新输入：')
            print('还没有写完呢')
    else:
        print('请先登陆！！')
        time.sleep(1)
        login()




def play():
    print('1、 注册')
    print('2、 登陆')
    print('3、 修改密码')
    print('4、 查看商品')
    print('q、 退出')
    i = input('请选择你的操作：')
    if i == '1':
        index()
    elif i == '2':
        login()
    elif i == '3':
        password()
    elif i == '4':
        other()
    elif i == 'q':
        exit
    else:
        play()
    
os.system('cls')
play()

