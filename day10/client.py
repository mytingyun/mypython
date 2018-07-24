# coding: utf-8

import socket




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
        msg = cli.recv(1024).decode('utf-8')
        print("服务器端消息：",msg)
        cli.send(b"uploading the file")
    elif select == '2':
        cli.send(select.encode('utf-8'))
        msg2 = cli.recv(1024).decode('utf-8')
        print("服务器端消息：", msg2)
        cli.send(b'I want download the files')
    elif select == '3':
        cli.send(select.encode('utf-8'))
        break
cli.close()

