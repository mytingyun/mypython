import socket
import json

serv = socket.socket()

serv.bind(('127.0.0.1',9001))
serv.listen()
conn,addr = serv.accept()
res = conn.recv(1024)
resu = res.decode('utf-8').split()
resu = resu[1].replace('?','').replace('&',' ').replace('/','')
# print(resu.split())
mydic = {}
for i in resu.split():
    mylist = i.split('=')
    mydic[mylist[0]]=mylist[1]
print(mydic)
with open('userinfo.txt','w+') as fi1:
    json.dump(mydic,fi1)
conn.close()
serv.close()

