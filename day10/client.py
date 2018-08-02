# coding: utf-8

import os,time
import socket
import hashlib
import struct
from server import sendstr,servstr

def cli_conn(n=1024):
    md5_obj = hashlib.md5()
    cli = socket.socket()
    cli.connect(('127.0.0.1',9002))
    while True:
        print("请可以操作：\n"
              "1、上传\n"
              "2、下载\n"
              "3、退出")
        select = input("请选择：").strip()
        if select == '1':
            #发送1到服务器端
            sendstr(cli,select.encode('utf-8'))
            msg = servstr(cli)
            print("服务器端消息：",msg)
            file1 = input("请输入要上传的文件名：")
            with open(file1, 'rb') as f1:
                file_size = os.path.getsize(file1)
                #获取文件大小并发送文件名给服务端
                sendstr(cli,file1.encode('utf-8'))
                #发送文件大小给服务端
                sendstr(cli,str(file_size).encode('utf-8'))
                #开始发送文件并获取md5值
                while file_size > 0:
                    content = f1.read(n)
                    md5_obj.update(content)
                    sendstr(cli,content)
                    file_size -= len(content)
                f1.close()
            #将本地获得的文件的md5值发送到服务器端
            md5s = md5_obj.hexdigest().encode('utf-8')
            sendstr(cli,md5s)
            print('本文件md5值是：',md5s)
        elif select == '2':
            # 发送2到服务器端
            sendstr(cli, select.encode('utf-8'))
            msg2 = servstr(cli)
            print("服务器端消息：", msg2)
            file2 = input("请输入要下载的文件名：")
            #发送要下载的文件名到服务端
            sendstr(cli,file2.encode('utf-8'))
            #接收文件大小
            filesize = servstr(cli)
            print("服务器端消息：要下载的文件大小是",filesize)
            filesize = int(filesize)
            file2 = file2+'down'
            f1 = open(file2, mode='wb')
            while filesize > 0:
                num = struct.unpack('i', cli.recv(4))[0]
                content = cli.recv(num)
                md5_obj.update(content)
                f1.write(content)
                filesize -= len(content)
            f1.close()
            remote_md5 = servstr(cli)
            local_md5 = md5_obj.hexdigest()
            if remote_md5 == local_md5:
                print("发送端的md5值和本地接收后的md5值相等，都是:", local_md5)
            else:
                print("发送端的md5是:", remote_md5)
                print("接收后的文件md5是：", local_md5)
        elif select == '3':
            sendstr(cli, select.encode('utf-8'))
            break
    cli.close()

if __name__ == '__main__':
    cli_conn()


