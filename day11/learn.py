
import threading
import time
from urllib import request

# req = request.Request(url)
# req.add_header('Range', 'bytes=0-1000')

# res = request.urlopen(req)
# with open('./b.gif', 'wb') as f:
#     f.write(res.read())

# print(f'文件大小：{get_size(url)} B') 



# print('主线程开始')

# def f1():
#     print('子线程 t1 已经开始')
#     for i in range(10):
#         print(i)
#         time.sleep(1)
#     print('子线程 t1 已经结束')

    
# # 创建一个线程对象 target 线程运行时要执行的操作
# t1 = threading.Thread(target=f1, name='t1')
# # 设置当前线程为 t1 的守护线程
# # 当前线程结束时 t1 也会结束
# t1.daemon = True
# # 启动线程
# t1.start()
# # 阻塞当前线程 直到 t1 结束才会继续执行后面的代码 (阻塞时间超过3秒)
# t1.join(3)
# print('主线程结束')




# 多线程下载

import threading
from urllib import request

data_d = {}

def download(url, t=1):
    size = get_size(url)
    print('总大小: ', size)
    t_size = size // t
    start = 0
    ts = []
    for i in range(t):
        end = t_size + start
        if end > size:
            end = size
        print(f'range[{start}, {end}]')
        t = threading.Thread(target=get_range, args=(url, start, end), name=str(i))
        ts.append(t)
        start = end + 1
        t.start()
    for t in ts:
        t.join()


def get_range_res(url, start, end):
    req = request.Request(url)
    req.add_header('Range', f'bytes={start}-{end}')
    res = request.urlopen(req)
    return res

def get_range(url, start, end):
    res = get_range_res(url, start, end)
    data = res.read()
    data_d[threading.current_thread().name] = data

def get_size(url):
    res = get_range_res(url, 0, 1)
    return int(res.headers['Content-Range'].split('/')[-1])

def save_data(path):
    for i in range(len(data_d)):
        with open(path, 'ab') as f:
            data = data_d[str(i)]
            f.write(data)

url = ''
download(url, 4)
save_data('./')