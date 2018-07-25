# coding: utf-8
import os
import socket
import hashlib

files = {'filename':'receive','filesize':0}

# def rece_file(filename,contact):
#     with open(filename,mode='ab') as f1:
#         f1.write(contact)



def serve_start():
    serv = socket.socket()
    serv.bind(('127.0.0.1',9001))
    serv.listen()
    while True:
        conn,addr = serv.accept()
        while True:
            res = conn.recv(1024)
            #print("res is:",res)
            if res == b'1':
                conn.send(b"please upload")
                filename = conn.recv(7)
                file1 = filename.decode('utf-8')
                files['filename'] = file1+'back'
                print('文件名是：',files['filename'])
                filesize = conn.recv(1024)
                files['filesize'] = filesize
                print("文件大小是：",files['filesize'])
                files['filesize'] = int(files['filesize'])
                f1 = open(files['filename'], mode='wb')
                while files['filesize'] > 0:
                    content = conn.recv(1024)
                    f1.write(content)
                    files['filesize'] -= 1024
                f1.close()
            if res == b'2':
                conn.send(b"ple select download filename")
                res = conn.recv(1024)
                print("客户端端消息：", res)
                file2 = conn.recv(1024)
            if res == b'3':
                break
        conn.close()
    serv.close()


if __name__ == '__main__':
    serve_start()




# import os
# import hashlib
# def get_md5(file,n = 10240):
#     with open(file, 'rb') as f1:
#         md5_obj = hashlib.md5()
#         file_size = os.path.getsize(file)
#         while file_size>0:
#             md5_obj.update(f1.read(n))
#             file_size -= n
#         return md5_obj.hexdigest()