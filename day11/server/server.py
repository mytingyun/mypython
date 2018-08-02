import os
import sys
import json
import struct
import hashlib
import socketserver

from ser_config import *



def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

class MyFTPServer(socketserver.BaseRequestHandler):
    # login 情况的静态变量
    def myrecv(self):
        dic_len = self.request.recv(4)
        dic_len = struct.unpack('i', dic_len)[0]
        dic = self.request.recv(dic_len).decode('utf-8')
        dic = json.loads(dic)
        return dic

    def send_dic(self,sk, dic):
        bytes_dic = json.dumps(dic).encode('utf-8')
        len_dic = struct.pack('i', len(bytes_dic))
        sk.send(len_dic)
        sk.send(bytes_dic)

    def login(self):
        dic = self.myrecv()
        name = dic['user']
        passwd = dic['password']
        with open("users.txt", encoding='utf-8', mode='r+') as file2:
            alluser = file2.readlines()
            index = 0
            for user in alluser:
                if name in user:
                    reault = alluser[index]
                    nowuser = reault.strip().split()
                    if passwd == nowuser[1]:
                        log_stat = {'user': nowuser[0], 'status': 'online'}
                        self.send_dic(self.request,log_stat)

                    else:
                        log_stat = {'user': nowuser[0], 'status': 'offline'}
                        self.send_dic(self.request, log_stat)

                if index == len(alluser)-1:
                    log_stat = {'user': None, 'status': 'nouser'}
                    self.send_dic(self.request,log_stat)
                    break
                index += 1


    def upload(self):
        # 接收要上传的文件信息
        # 再接收文件
        md5 = hashlib.md5()
        dic = self.myrecv()
        # {'filename':file,'filesize':71827}
        with open(os.path.join('upload',dic['filename']),'wb') as f:
            while dic['filesize'] > 0 :
                content = self.request.recv(read_rize)
                md5.update(content)
                f.write(content)
                dic['filesize'] -= len(content)
        md5code = md5.hexdigest()
        dic = self.myrecv()
        print(dic['md5code'] , md5code)
        if  dic['md5code'] == md5code:
            self.request.send('上传成功'.encode('utf-8'))
    def download(self):
        md5 = hashlib.md5()
        dic = self.myrecv()
        file_path = os.path.join('upload', dic['filename'])
        filesize = os.path.getsize(file_path)
        sizedic = {'filesize': filesize}
        self.send_dic(self.request,sizedic)
        print('file size:', filesize)
        with open(file_path, 'rb') as f:
            while filesize > 0:
                content = f.read(read_rize)
                md5.update(content)
                self.request.send(content)
                filesize -= len(content)
        md5code = md5.hexdigest()
        dic = {'md5code': md5code}
        self.send_dic(self.request, dic)
        print("md5 is:",md5code)
        self.request.send(md5code.encode('utf-8'))

    def handle(self):
        operate = self.request.recv(read_rize).decode('utf-8')
        # {'operate':'upload','name':''} 'download'
        func = getattr(self,operate)
        func()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(connect,MyFTPServer)
    server.serve_forever()

