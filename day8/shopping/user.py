
import csv

class User:
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return f'用户: {self.username}'

def get_all_users():
    with open('./day8/shopping/user.csv', 'r', encoding='utf-8') as f:
        l = list(csv.reader(f))[1:]
        users = []
        for i in l:
            user = User(*i)
            users.append((user.username, user.password))
    return users

def get_all_usernames():
    users = get_all_users()
    usernames =[]
    for i in users:
        usernames.append(i[0])
    return usernames

def is_in_csv(username):
    usernames = get_all_usernames()
    if username in usernames:
        return True
    else:
        return False

def insert(username, password):
    with open('./day8/shopping/user.csv', 'a+', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow([username,password])

def login(username, password):
    users = get_all_users()
    if (username, password) in users:
        return True
    else:
        return False

# def updata_password(password, new_password):


# register('xiaol', '123')