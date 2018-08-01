import os
import sys
import json
import struct
import socket
import hashlib
from cli_config import *

def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

def send_dic(sk,dic):
    bytes_dic = json.dumps(dic).encode('utf-8')
    len_dic = struct.pack('i', len(bytes_dic))
    sk.send(len_dic)
    sk.send(bytes_dic)

def myrecv(sk):
    dic_len = sk.recv(4)
    dic_len = struct.unpack('i', dic_len)[0]
    dic = sk.recv(dic_len).decode('utf-8')
    dic = json.loads(dic)
    return dic

def wrapper(f):
    def inner(*args,**kwargs):
        if log_stat["status"] == 'online':
            f(*args,**kwargs)
        else:
            print("您尚未登陆，请先登陆。。。")
            return False
    return inner

def login(sk):
    md5 = hashlib.md5()
    user = input("user: ")
    password = input("password: ")
    md5.update(password.encode('utf-8'))
    md5pwd = md5.hexdigest()
    userinfo = {'user': user, 'password':md5pwd}
    send_dic(sk,userinfo)

def upload(sk):
    # 上传这个操作
    # 要上传的文件信息
    # 文件(大文件)
    # 上传成功
    md5 = hashlib.md5()
    sk.send(b'upload')
    file_path = input('filepath : ')
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)
    origin_filesize = filesize
    dic = {'filename': filename, 'filesize': filesize}
    send_dic(sk,dic)
    with open(file_path,'rb') as f:
        while filesize > 0:
            content = f.read(read_rize)
            md5.update(content)
            sk.send(content)
            filesize -= len(content)
            processBar(origin_filesize-filesize,origin_filesize)
    md5code = md5.hexdigest()
    dic = {'md5code': md5code}
    send_dic(sk, dic)
    result = sk.recv(read_rize)
    print(result.decode('utf-8'))

def download(sk):
    md5 = hashlib.md5()
    sk.send(b'download')
    filename = input('filename : ')
    dic = {'filename': filename}
    send_dic(sk, dic)
    size = myrecv(sk)
    origin_filesize = size['filesize']
    with open(os.path.join('upload', filename), 'wb') as f:
        while size['filesize'] > 0:
            content = sk.recv(read_rize)
            md5.update(content)
            f.write(content)
            size['filesize'] -= len(content)
            processBar(origin_filesize - size['filesize'], origin_filesize)
    md5code = md5.hexdigest()
    md5dic = myrecv(sk)

    if md5dic['md5code'] == md5code:
        print("下载成功")
    else:
        print("server md5:",md5dic)
        print("local md5:",md5code)

log_stat = {'user': None,'status': 'offline'}

if __name__ == '__main__':
    sk = socket.socket()
    sk.connect(connect)
    choices_lst= [('登录',login),('上传',upload),('下载',download)]
    while True:
        for num,item in enumerate(choices_lst,1):
            print(num,item[0])
        num = int(input('num >>> '))
        choices_lst[num-1][1](sk)


















