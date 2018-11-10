import socket
import json
import pymysql

serv = socket.socket()
ip = '172.17.2.214'

conns = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password="123456",
    database='mydb',
    port=3306,
    charset='utf8'

)
cur = conns.cursor()

talbessql = 'show tables;'
builed_talbe = 'create table users(id int(4) not null primary key auto_increment,name varchar(10) not null,password int(50) not null) charset=utf8;'
insertsql = "insert into users(name,password) values (%(name)s,%(password)s)"

user = 'myuser'
pwd = '123456'

resultNum = cur.execute(talbessql)
rows = cur.fetchall()
try:
	if  rows[0]:
		print("users table is exist",rows)
except (KeyboardInterrupt,IndexError):
	cur.execute(builed_talbe)
	print("users table is not exist, builded success!")

results = cur.execute(insertsql,{"name":user,"password":pwd})
print(results)

conns.commit()
cur.close()


serv.bind((ip,9001))
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
print('登陆的用户名密码是：',mydic)
with open('userinfo.txt','w+') as fi1:
    json.dump(mydic,fi1)
conn.close()
serv.close()

cur2 = conns.cursor()
selectsql = 'select * from users;'
result2 = cur2.execute(selectsql)
alldata = cur2.fetchone()
print('数据库数据是：',alldata)

if mydic['username'] == alldata[1] and int(mydic['pwd']) == alldata[2]:
	print("login success")
else:
	print("login failed")


cur2.close()
conns.close()
