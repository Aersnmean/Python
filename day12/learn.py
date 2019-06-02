
import sqlite3

# # 1.连接数据库
# sql_connect = sqlite3.connect('./day12/test.db')
# # 2.获取 cursor
# sql_cursor = sql_connect.cursor()
# # 3.执行 sql 命令, 创建一个 table
# # sql_cursor.execute('create table users (name verchar(255) not null, age integer);')
# # 4.执行 sql 命令, 插入数据
# # 增 insert
# # sql_cursor.execute('insert into users values ("浩浩", 18);')
# # sql_cursor.execute('insert into users (name, age) values ("菲菲", 19);')
# # sql_cursor.execute('insert into users (name) values ("以撒");')

# # 删 delete
# # sql_cursor.execute('delete from users where "name" = "浩浩";')

# # 改 update
# # sql_cursor.execute('update users set age = 7 where name = "以撒";')
# # sql_cursor.execute('update users set name = "莉莉丝" where name = "菲菲" and age = 19;')

# # 查 select
# sql_cursor.execute('select * from users;')

# # 5.查询完毕获取结果集
# data = sql_cursor.fetchall()
# print(type(data), data)

# # 提交操作
# sql_connect.commit()
# # 收尾操作 关闭数据库
# sql_cursor.close()
# sql_connect.close()

