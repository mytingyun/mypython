import os
import json
import struct
import hashlib
import socketserver

class MyFTPServer(socketserver.BaseRequestHandler):
    # login 情况的静态变量
    def myrecv(self):
        dic_len = self.request.recv(4)
        dic_len = struct.unpack('i', dic_len)[0]
        dic = self.request.recv(dic_len).decode('utf-8')
        dic = json.loads(dic)
        return dic
    def upload(self):
        # 接收要上传的文件信息
        # 再接收文件
        md5 = hashlib.md5()
        dic = self.myrecv()
        # {'filename':file,'filesize':71827}
        with open(os.path.join('upload',dic['filename']),'wb') as f:
            while dic['filesize'] > 0 :
                content = self.request.recv(1024)
                md5.update(content)
                f.write(content)
                dic['filesize'] -= len(content)
        md5code = md5.hexdigest()
        dic = self.myrecv()
        print(dic['md5code'] , md5code)
        if  dic['md5code'] == md5code:
            self.request.send('上传成功'.encode('utf-8'))

    def handle(self):
        operate = self.request.recv(1024).decode('utf-8')   # 'upload'
        # {'operate':'upload','name':''} 'download'
        func = getattr(self,operate)
        func()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyFTPServer)
    server.serve_forever()

# 一个核心功能 上传
# 辅助
