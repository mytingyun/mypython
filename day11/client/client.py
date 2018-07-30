import os
import sys
import json
import struct
import socket
import hashlib

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

def download():
    pass

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
            content = f.read(1024)
            md5.update(content)
            sk.send(content)
            filesize -= len(content)
            processBar(origin_filesize-filesize,origin_filesize)
    md5code = md5.hexdigest()
    dic = {'md5code': md5code}
    send_dic(sk, dic)
    result = sk.recv(1024)
    print(result.decode('utf-8'))

if __name__ == '__main__':
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    choices_lst= [('上传',upload),('下载',download)]
    while True:
        for num,item in enumerate(choices_lst,1):
            print(num,item[0])
        num = int(input('num >>> '))
        choices_lst[num-1][1](sk)

















