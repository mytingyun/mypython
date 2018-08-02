# coding: utf-8
import os,time
import socket
import hashlib
import struct

files = {'filename':'receive','filesize':0}

def sendstr(handle,content):
    lenb = struct.pack('i', len(content))
    handle.send(lenb + content)

def servstr(handle):
    num = struct.unpack('i', handle.recv(4))[0]
    message = handle.recv(num).decode('utf-8')
    return message

def serve_start(n=1024):
    md5_obj = hashlib.md5()
    serv = socket.socket()
    serv.bind(('127.0.0.1',9002))
    serv.listen()
    while True:
        conn,addr = serv.accept()
        while True:
            res = servstr(conn)
            #根据客户端发送的消息进行选择上传还是下载
            if res == '1':
                hint = b"please upload"
                sendstr(conn,hint)
                #接收文件名
                file1 = servstr(conn)
                files['filename'] = file1+'upload'
                print('文件名是：',files['filename'])
                #接收文件大小
                filesize = servstr(conn)
                files['filesize'] = filesize
                print("文件大小是：",files['filesize'])
                files['filesize'] = int(files['filesize'])
                with open(files['filename'], mode='wb') as f1:
                    while files['filesize'] > 0:
                        #开始接收文件并计算文件md5值
                        num = struct.unpack('i', conn.recv(4))[0]
                        content = conn.recv(num)
                        md5_obj.update(content)
                        f1.write(content)
                        files['filesize'] -= len(content)
                #接收客户端的md5值
                remote_md5 = servstr(conn)
                #算出本地md5值
                local_md5 = md5_obj.hexdigest()
                #将本地计算的md5值和客户端值的md5值进行比较
                if remote_md5 == local_md5:
                    print("发送端的md5值和本地接收后的md5值相等，都是:",local_md5)
                else:
                    print("发送端的md5是:", remote_md5)
                    print("接收后的文件md5是：", local_md5)
            if res == '2':
                mess = b"ple select download filename"
                sendstr(conn,mess)
                file2 = servstr(conn)
                print("客户端端消息：要下载的文件是 ", file2)
                with open(file2, 'rb') as f2:
                    file_size = os.path.getsize(file2)
                    print('file size is',file_size)
                    sendstr(conn,str(file_size).encode('utf-8'))
                    while file_size > 0:
                        content = f2.read(n)
                        md5_obj.update(content)
                        sendstr(conn,content)
                        file_size -= len(content)
                md5s = md5_obj.hexdigest().encode('utf-8')
                sendstr(conn,md5s)
                print("本地文件md5值是：",md5s)
            if res == '3':
                break
        conn.close()
    serv.close()


if __name__ == '__main__':
    serve_start()


