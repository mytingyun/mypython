# coding: utf-8
import time,hashlib
import os,sys

bash_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(bash_dir)



log_status = {"username": None,"status": False,"identity": None}


def mymd5(strs):
    md5obj = hashlib.md5()
    md5obj.update(strs.encode('utf-8'))
    return md5obj.hexdigest()

# print(mymd5('789'))

def login():
    name = input("请输入你的用户名： ").strip()
    with open("%s/db/user.txt" %bash_dir,encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[index]
            nowuser = reault.strip().split()
            while True:
                passwds = input("please input your password: ").strip()
                passwd = mymd5(passwds)
                if passwd == nowuser[1]:
                    print("%s login success" %name)
                    log_status["username"] = name
                    log_status["status"] = True
                    log_status["identity"] = nowuser[2]
                    return log_status
                else:
                    pwd+=1
                    print("your passwd is error, please retry...")
                    if pwd == 3:
                        print("your input password error thrice, your account locked")
                        exit()
                    continue
        if index == len(alluser)-1:
            print("your name is not exist,please contact admin!!")
            break
        index += 1

def wrapper(f):
    def inner(*args,**kwargs):
        if log_status["status"]:
            ret = f(*args,**kwargs)
            return ret
        else:
            print("您尚未登陆，请先登陆。。。")
            return False
    return inner

# login()