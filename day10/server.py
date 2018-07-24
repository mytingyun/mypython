# coding: utf-8

import socket

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
            res = conn.recv(1024)
            print("客户端端消息：", res)
        if res == b'2':
            conn.send(b"ple select download filename")
            res = conn.recv(1024)
            print("客户端端消息：", res)
        if res == b'3':
            break
    conn.close()
serv.close()



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