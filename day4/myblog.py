#!/usr/bin/env python
# encoding: utf-8
global session
session = 0
def register():
    file1 = open('username.txt',encoding='utf-8',mode='a+')
    file1.seek(0)
    nowuser = file1.read()
    #print('now user is:', nowuser)
    while True:
        user = input("please input your name: ")
        passwd1 = input("please input your passwd: ")
        passwd2 = input("please again input your passwd: ")
        if user in nowuser:
            print("your name is exist, please again input...")
            continue
        elif passwd1 != passwd2:
            print("you input twice password different, please again again input...")
            continue
        else:
            file1.write('\n%s  %s' %(user, passwd1))
            break
    return "%s user register success, please login..." %user


def login(name):
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[index]
            nowuser = reault.strip().split()
            #print("nowuser is: ",nowuser)
            while True:
                passwd = input("please input your password: ")
                if passwd == nowuser[1]:
                    print("login success")
                    session = 'success'
                    return session
                else:
                    pwd+=1
                    print("your passwd is error, please retry...")
                    if pwd == 3:
                        print("your input password error thrice, your account locked")
                        exit()
                    continue
        if index == len(alluser)-1:
            print("your name is not exist,please register")
            break
        index += 1

def article():
    print("欢迎来到文章页面。。。。")

def diary():
    print("欢迎来到日记页面。。。。")

def comment():
    print("欢迎来到评论页面。。。。")

def enshrine():
    print("欢迎来到收藏页面。。。。")

while True:
    print("what are you doing: \n"
          "1、登陆\n"
          "2、注册\n"
          "3、退出")
    do = input("please select number: ")
    do = int(do)
    if do == 1:
        name = input("please input your name for login: ")
        set = login(name)
        if set == 'success':
            print("1、购物\n"
                  "2、返回上级菜单")
            select = input("please select number: ")
            if int(select) == 1:
                shopping()
            elif select == 2:
                exit()
    elif do == 2:
        status = register()
        print(status)
    elif do == 3:
        exit()
    else:
        print("input error, please reatry...")


