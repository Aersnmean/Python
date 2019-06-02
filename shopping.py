import functools
import datetime
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
    global information
    user = input('请输入用户名：')
    password = input('请输入密码：')
    for find in information:
        if user is find['user']:
            print('该用户名已存在，请重新输入：')
            index()
    
    information.append({'user': user, 'password': password})
    print(f'恭喜{user}注册成功!!')
    play()
def login():
    global information
    global judg
    in_user = input('用户名：')
    in_password = input('密码：')
    for find in information:
        if in_user == find['user'] and in_password == find['password']:
            print(f'欢迎{in_user}光临！！')
            judg = 1
            play()
        else:
            print('Sorry,密码没连接成功')
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
    j = 1
    for i in comment:
        print(f"{j}、{i['name']}, {i['count']}, {i['pric']}", sep = '   ')
        j += 1
    if judg :
        shopping = int(input('请输入要购买商品的标号：'))
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
        login()




def play():
    print('1、注册')
    print('2、登陆')
    print('3、修改密码')
    print('4、查看商品')
    i = int(input('请选择你的操作：'))
    [index() if i == 1 else (login() if i == 2 else (password() if i == 3 else other()))]
    
play()
