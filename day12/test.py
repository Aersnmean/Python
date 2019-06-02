
import sqlite3

class hahaSQL:

    @staticmethod
    def open(path):
        return hahaSQL(path)

    def __init__(self, path):
        self.path = path
    
    def insert(self, tb_name, *args, **kwargs):
        sql_cmd = f'insert into {tb_name} '
        if args:
            sql_cmd += f'values ({str(list(args)).strip("[]")})'
        elif kwargs:
            k = str(list(kwargs.keys())).replace("'", '').strip('[]')
            v = str(list(kwargs.values())).strip('[]')
            sql_cmd += f'({k}) values ({v})'
        self.exec(sql_cmd)
    
    def delete(self, tb_name, **kwargs):
        sql_cmd = f'delete from {tb_name}'
        if kwargs:
            sql_cmd += ' where'
            for k, v in kwargs.items():
                vv = str(v)
                if type(v) is str:
                    vv = '"' + v + '"'
                sql_cmd += ' ' + k + '=' + vv + ' and'
        sql_cmd = sql_cmd[:-4]
        self.exec(sql_cmd)
    
    def update(self, tb_name, *args, **kwargs):
        sql_cmd = f'delete from {tb_name}'
        # 拼接 SQL 命令字符串 
        if kwargs: 
            sql_cmd += ' where'
            for k, v in kwargs.items():
                vv = str(v)
                if type(v) is str:
                    vv = '"' + v + '"'
                sql_cmd += ' ' + k + '=' + vv + ' and'
        sql_cmd = sql_cmd[:-4]

        self.exec(sql_cmd)
    
    def select(self, tb_name):
        sql_cmd = f'select from {tb_name}'
        # 拼接 SQL 命令字符串

        self.exec(sql_cmd)
        return self.cursor.fetchall()

    def exec(self, sql_cmd):
        self.cursor.execute(sql_cmd)
        self.connect.commit()

    def __enter__(self):
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()
        return self
    
    def __exit__(self, *args):
        self.cursor.close()
        self.connect.close()

with hahaSQL.open('./day12/test.db') as sql:
    sql.insert('users', '哈哈', 66)


