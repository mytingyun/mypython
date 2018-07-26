# coding: utf-8

import os,time
import socket
import hashlib

def get_md5(file,n = 10240):
    with open(file, 'rb') as f1:
        md5_obj = hashlib.md5()
        file_size = os.path.getsize(file)
        while file_size>0:
            md5_obj.update(f1.read(n))
            file_size -= n
        return md5_obj.hexdigest()


def cli_conn(n=1024):
    cli = socket.socket()
    cli.connect(('127.0.0.1',9001))
    while True:
        print("请可以操作：\n"
              "1、上传\n"
              "2、下载\n"
              "3、退出")
        select = input("请选择：").strip()
        if select == '1':
            cli.send(select.encode('utf-8'))
            file1 = input("请输入要上传的文件名：")
            msg = cli.recv(1024).decode('utf-8')
            print("服务器端消息：",msg)
            with open(file1, 'rb') as f1:
                file_size = os.path.getsize(file1)
                cli.send(file1.encode('utf-8'))
                cli.send(str(file_size).encode('utf-8'))
                time.sleep(0.5)
                while file_size > 0:
                    content = f1.read(n)
                    cli.send(content)
                    file_size -= n
        elif select == '2':
            cli.send(select.encode('utf-8'))
            msg2 = cli.recv(1024).decode('utf-8')
            print("服务器端消息：", msg2)
            file2 = input("请输入要下载的文件名：")
            cli.send(file2.encode('utf-8'))
            filesize = cli.recv(1024)
            print("服务器端消息：要下载的文件大小是",filesize)
            filesize = int(filesize)
            file2 = file2+'rece'
            f1 = open(file2, mode='wb')
            while filesize > 0:
                content = cli.recv(1024)
                f1.write(content)
                filesize -= 1024
            f1.close()
            # cli.send(b'I want download the files')
        elif select == '3':
            cli.send(select.encode('utf-8'))
            break
    cli.close()

if __name__ == '__main__':
    cli_conn()
