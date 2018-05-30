#!/usr/bin/env python
# encoding: utf-8

log_status = {"username": None,"status": False}
def register():
    file1 = open('username.txt',encoding='utf-8',mode='a+')
    file1.seek(0)
    nowuser = file1.read()
    while True:
        user = input("please input your name: ").strip()
        passwd1 = input("please input your passwd: ").strip()
        passwd2 = input("please again input your passwd: ").strip()
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


def login():
    name = input("请输入你的用户名： ").strip()
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[index]
            nowuser = reault.strip().split()
            while True:
                passwd = input("please input your password: ").strip()
                if passwd == nowuser[1]:
                    print("login success")
                    log_status["username"] = name
                    log_status["status"] = True
                    return log_status
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

def wrapper(f):
    def inner(name,status,*args,**kwargs):
        if name and status:
            ret = f(name,status,*args,**kwargs)
        else:
            print("您尚未登陆，请先登陆。。。")
            login()
        return ret
    return inner


@wrapper
def article(username,status):
    print("欢迎%s来到文章页面。。。。" %username)
@wrapper
def diary(username,status):
    print("欢迎%s来到日记页面。。。。" %username)
@wrapper
def comment(username,status):
    print("欢迎%s来到评论页面。。。。" %username)
@wrapper
def enshrine(username,status):
    print("欢迎%s来到收藏页面。。。。" %username)


def logout():
    log_status["username"] = None
    log_status["status"] = False
    print("您已注销")


funcs= {1: login, 2: register, 3: article, 4: diary, 5: comment, 6: enshrine, 7: logout, 8: exit}

while True:
    print("欢迎来到博客园首页: \n"
          "1、登陆\n"
          "2、注册\n"
          "3、文章页面\n"
          "4、日记页面\n"
          "5、评论页面\n"
          "6、收藏页面\n"
          "7、注销\n"
          "8、退出程序")
    selectnum = input("please select number: ").strip()
    try:
        if 0 < int(selectnum) <=len(funcs):
            funcs[int(selectnum)](log_status["username"],log_status["status"])
        else:
            print("您输入的超出范围")
    except ValueError as err:
        print("您输入有误，请输入1-8的数字")

