# encoding: utf-8

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
    return "%s user register success" %user
status = register()
print(status)

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
                    exit()
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

name = input("your name: ")
login(name)

