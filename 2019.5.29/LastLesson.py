# requests
import requests, os, time

location_url = r'http://v.juhe.cn/weather/geo'
img_url = r'http://39.96.4.131/media/190529145637870.png'

class Download:

    @property
    def url(self): return self.__url
    @property
    def save_path(self): return self.__save_path
    @property
    def file_size(self): return self.__file_size
    @property
    def did_downloaded_size(self): return self.__did_downloaded_size
    @property
    def did_exists(self): return self.__did_exists
    @property
    def download_step(self): return self.__download_step
    @download_step.setter
    def download_step(self, v): self.__download_step = v
    @property
    def speed(self): return self.__speed
    @property
    def res_head(self): return self.__res_head
    def __init__(self, url, save_path):
        self.did_finished = None
        self.will_begin = None
        self.on_download = None
        self.__url = url
        self.__speed = 0
        self.__save_path = save_path
        self.__res_head = requests.head(self.__url).headers
        self.__file_size = int(self.__res_head['Content-Length'])
        self.__did_exists = False
        self.__did_downloaded_size = 0
        self.__download_step = 10000
        if os.path.exists(self.__save_path):
            self.__did_downloaded_size = os.path.getsize(self.__save_path)
            self.__did_exists = True
    def Start(self):
        res_header = {}
        res_header['Range'] = f'bytes={self.__did_downloaded_size}-{self.__file_size}'
        res = requests.get(self.__url, stream=True, headers=res_header)
        # with open(self.__save_path, 'ab') as f:
        #     if self.will_begin:
        #         self.will_begin()
        #     last_t = time.time()
        #     s_down_size = 0
        #     for content in res.iter_content(self.__download_step):
        #         f.write(content)
        #         self.__did_downloaded_size += len(content)
        #         s_down_size += len(content)
        #         if time.time() - last_t >= 0.1:
        #             self.__speed = s_down_size / (time.time() - last_t)
        #             s_down_size = 0
        #             last_t = time.time()
        #         if self.on_download:
        #             self.on_download(self)
        self.__speed = 0
        if self.did_finished:
            self.did_finished()
        
def downloading(obj: Download):
    print(f'\r{obj.did_downloaded_size / 1000:.0f} / {obj.file_size / 1000:.0f} KB - {obj.did_downloaded_size / obj.file_size:.0%}  {obj.speed / 1000:.0f} KB/s', end='')

xunlei_url = r'http://down.sandai.net/thunderx/XunLeiWebSetup10.1.13.418dl.exe'
d = Download(xunlei_url, './迅雷.exe')
print(d.file_size)
d.will_begin = lambda : print('开始下载')
d.on_download = downloading
d.did_finished = lambda : print('下载完毕')
d.Start()