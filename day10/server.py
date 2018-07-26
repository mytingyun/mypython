# coding: utf-8
import os,time
import socket
import hashlib

files = {'filename':'receive','filesize':0}


def serve_start(n=1024):
    md5_obj = hashlib.md5()
    serv = socket.socket()
    serv.bind(('127.0.0.1',9002))
    serv.listen()
    while True:
        conn,addr = serv.accept()
        while True:
            res = conn.recv(1024)
            #根据客户端发送的消息进行选择上传还是下载
            if res == b'1':
                conn.send(b"please upload")
                #接收文件名
                filename = conn.recv(1024)
                time.sleep(0.2)
                file1 = filename.decode('utf-8')
                files['filename'] = file1+'back'
                print('文件名是：',files['filename'])
                #接收文件大小
                filesize = conn.recv(1024)
                time.sleep(0.2)
                files['filesize'] = filesize
                print("文件大小是：",files['filesize'])
                files['filesize'] = int(files['filesize'])
                with open(files['filename'], mode='wb') as f1:
                    while files['filesize'] > 0:
                        #开始接收文件并计算文件md5值
                        content = conn.recv(1024)
                        md5_obj.update(content)
                        f1.write(content)
                        files['filesize'] -= 1024
                #接收客户端的md5值
                remote_md5 = conn.recv(1024)
                #算出本地md5值
                local_md5 = md5_obj.hexdigest()
                #将本地计算的md5值和客户端值的md5值进行比较
                if remote_md5.decode('utf-8') == local_md5:
                    print("发送端的md5值和本地接收后的md5值相等，都是:",local_md5)
                else:
                    print("发送端的md5是:", remote_md5)
                    print("接收后的文件md5是：", local_md5)
            if res == b'2':
                conn.send(b"ple select download filename")
                file2 = conn.recv(1024)
                print("客户端端消息：要下载的文件是 ", file2)
                file2 = file2.decode('utf-8')
                with open(file2, 'rb') as f2:
                    file_size = os.path.getsize(file2)
                    print('file size is',file_size)
                    conn.send(str(file_size).encode('utf-8'))
                    time.sleep(1)
                    while file_size > 0:
                        content = f2.read(n)
                        md5_obj.update(content)
                        conn.send(content)
                        file_size -= n
                time.sleep(1)
                md5s = md5_obj.hexdigest().encode('utf-8')
                conn.send(md5s)
                print("本地文件md5值是：",md5s)
            if res == b'3':
                break
        conn.close()
    serv.close()


if __name__ == '__main__':
    serve_start()


