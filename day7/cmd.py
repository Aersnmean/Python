
import os

def main_loop():
    while True:
        content = input('请输入内容(输入exit退出): ')
        if content == 'exit':
            break
        # 以下开始执行用户的命令
        if not Command.run(content):
            print(f'无效命令 {content}')

class Command:

    cmds = []

    @classmethod
    def register(cls, c):
        Command.cmds.append(c)

    @classmethod
    def run(cls, c):
        cmd_l = c.split(' ')
        cmd_name = cmd_l[0]
        for c in Command.cmds:
            if c.cmd == cmd_name:
                return c.exec(*(cmd_l[1:]))

    def __init__(self, cmd, work):
        self.cmd = cmd
        self.work = work
    
    def exec(self, *args):
        if self.work:
            return self.work(*args)

def Cmd(name):
    def _Cmd(func):
        Command.register(Command(name, func))
        return func
    return _Cmd

@Cmd('ls')
def ls(*args):
    l = os.listdir(os.getcwd())
    for i in l:
        print(i)
    return True

@Cmd('cd')
def cd(*args):
    p = args[0]
    if not os.path.isabs(p):
        p = os.path.join(os.getcwd(), p)
    os.chdir(p)
    return True

@Cmd('touch')
def touch(*args):
    p = args[0]
    f = open(p, 'w')
    f.close()
    return True

@Cmd('mv')
def mv(*args):
    p1 = args[0]
    p2 = args[1]
    os.renames(p1, p2)
    return True

if __name__ == '__main__':
    main_loop()

